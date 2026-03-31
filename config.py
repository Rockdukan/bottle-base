import logging
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MEDIA_DIR = os.path.join(BASE_DIR, "media")
STATIC_DIR = os.path.join(BASE_DIR, "static")

LOG_DIR = os.path.join(BASE_DIR, "logs")
LOG_FILE = os.path.join(LOG_DIR, "app.log")

LOG_LEVEL_NAME = os.environ.get("LOG_LEVEL", "WARNING").upper()
LOG_LEVEL = getattr(logging, LOG_LEVEL_NAME, logging.WARNING)
LOG_BACKUP_DAYS = 7
LOG_CONSOLE = True
LOG_CONSOLE_COLOR = True

TEMPLATE_DIR = os.path.join(BASE_DIR, "app", "views")

HOST = os.environ.get("HOST", "127.0.0.1")
PORT = int(os.environ.get("PORT", "8080"))
DEBUG = os.environ.get("DEBUG", "true").lower() in ("1", "true", "yes", "on")
RELOADER = os.environ.get("RELOADER", "true").lower() in ("1", "true", "yes", "on")

CSRF_COOKIE_NAME = os.environ.get("CSRF_COOKIE_NAME", "csrf_token")
CSRF_FORM_FIELD = os.environ.get("CSRF_FORM_FIELD", "csrf_token")
CSRF_COOKIE_MAX_AGE = int(os.environ.get("CSRF_COOKIE_MAX_AGE", str(60 * 60 * 24 * 7)))
CSRF_COOKIE_HTTPONLY = os.environ.get("CSRF_COOKIE_HTTPONLY", "true").lower() in ("1", "true", "yes", "on")
CSRF_COOKIE_SECURE = os.environ.get("CSRF_COOKIE_SECURE", "false").lower() in ("1", "true", "yes", "on")
CSRF_COOKIE_SAMESITE = os.environ.get("CSRF_COOKIE_SAMESITE", "Lax")
