"""
Модуль для настройки веб-приложения с исправлением кодировки и CSRF защитой.

Этот модуль содержит конфигурацию Bottle приложения с патчами для корректной
обработки UTF-8 кодировки в формах и реализацией CSRF токенов для защиты
от межсайтовых атак.
"""
import secrets

from bottle import Bottle, FormsDict, TEMPLATE_PATH, request, abort

from config import TEMPLATE_DIR


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
            return value.encode('latin-1').decode('utf-8')
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
    Генерирует CSRF токен и сохраняет его в сессии.

    Если токен уже существует в сессии, возвращает существующий.
    Если токена нет, генерирует новый 32-символьный hex токен.

    Returns:
        str: CSRF токен из сессии.

    Note:
        Требует настроенную сессию Beaker в request.environ.
    """
    if 'csrf_token' not in request.environ.get('beaker.session', {}):
        request.environ['beaker.session']['csrf_token'] = secrets.token_hex(16)
    return request.environ['beaker.session']['csrf_token']


def validate_csrf_token():
    """
    Валидирует CSRF токен из формы против токена из сессии.

    Raises:
        HTTPError: 403 ошибка, если токены не совпадают или отсутствуют.

    Note:
        Ожидает токен в поле формы 'csrf_token' и сохраненный токен в сессии.
    """
    token = request.forms.get('csrf_token')
    session_token = request.environ.get('beaker.session', {}).get('csrf_token')
    if not token or token != session_token:
        abort(403, "CSRF токен недействителен")


app = Bottle()
TEMPLATE_PATH.insert(0, TEMPLATE_DIR)
