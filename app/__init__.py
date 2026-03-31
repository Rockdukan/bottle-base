"""
Модуль для настройки веб-приложения с исправлением кодировки и CSRF защитой.

Этот модуль содержит конфигурацию Bottle приложения с патчами для корректной
обработки UTF-8 кодировки в формах и реализацией CSRF токенов для защиты
от межсайтовых атак.
"""
import secrets

from bottle import abort, Bottle, FormsDict, TEMPLATE_PATH, request, response

from config import (
    CSRF_COOKIE_HTTPONLY,
    CSRF_COOKIE_MAX_AGE,
    CSRF_COOKIE_NAME,
    CSRF_COOKIE_SECURE,
    CSRF_COOKIE_SAMESITE,
    CSRF_FORM_FIELD,
    TEMPLATE_DIR,
)


def fix_encoding(value):
    """
    Исправляет кодировку строковых значений с latin-1 на utf-8.

    Args:
        value: Значение для исправления кодировки. Может быть любого типа.

    Returns:
        str или исходный тип: Строка с исправленной кодировкой или исходное значение,
        если это не строка или произошла ошибка декодирования.
    """

    if isinstance(value, str):

        try:
            return value.encode("latin-1").decode("utf-8")
        except (UnicodeDecodeError, UnicodeEncodeError):
            return value
    return value


# Патчим метод получения значений из форм
original_get = FormsDict.get


def patched_get(self, key, default=None):
    """
    Патченый метод получения значений из форм с исправлением кодировки.

    Args:
        self: Экземпляр FormsDict.
        key (str): Ключ для получения значения из формы.
        default: Значение по умолчанию, если ключ не найден.

    Returns:
        Значение из формы с исправленной кодировкой.
    """
    value = original_get(self, key, default)
    return fix_encoding(value)


# Применяем патч к классу FormsDict
FormsDict.get = patched_get


def generate_csrf_token():
    """
    Генерирует или переиспользует CSRF токен и сохраняет его в cookie.

    При первом обращении токен создается случайным образом и записывается в cookie.
    Токен возвращается вызывающей стороне для вставки в формы.

    Returns:
        str: CSRF токен.

    Notes:
        Cookie устанавливается через ``response.set_cookie`` и доступна только приложению.
    """

    token = request.get_cookie(CSRF_COOKIE_NAME)

    if not token:
        token = secrets.token_hex(16)
        response.set_cookie(
            CSRF_COOKIE_NAME,
            token,
            max_age=CSRF_COOKIE_MAX_AGE,
            httponly=CSRF_COOKIE_HTTPONLY,
            secure=CSRF_COOKIE_SECURE,
            samesite=CSRF_COOKIE_SAMESITE,
        )

    return token


def validate_csrf_token():
    """
    Валидирует CSRF токен из формы против токена из cookie.

    Raises:
        HTTPError: 403 ошибка, если токены отсутствуют или не совпадают.

    Notes:
        Ожидает токен в поле формы по имени ``CSRF_FORM_FIELD`` и сравнивает его с cookie.
    """

    token_from_form = request.forms.get(CSRF_FORM_FIELD)
    token_from_cookie = request.get_cookie(CSRF_COOKIE_NAME)

    if (
        not token_from_form
        or not token_from_cookie
        or token_from_form != token_from_cookie
    ):
        abort(403, "CSRF токен недействителен")


app = Bottle()
TEMPLATE_PATH.insert(0, TEMPLATE_DIR)
