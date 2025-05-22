from bottle import Bottle, FormsDict, TEMPLATE_PATH

from config import TEMPLATE_DIR


# Исправляем декодирование
def fix_encoding(value):
    if isinstance(value, str):
        try:
            return value.encode('latin-1').decode('utf-8')
        except (UnicodeDecodeError, UnicodeEncodeError):
            return value
    return value

# Патчим метод получения значений из форм
original_get = FormsDict.get

def patched_get(self, key, default=None):
    value = original_get(self, key, default)
    return fix_encoding(value)

FormsDict.get = patched_get

app = Bottle()

TEMPLATE_PATH.insert(0, TEMPLATE_DIR)
