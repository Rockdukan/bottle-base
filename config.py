import logging
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MEDIA_DIR = os.path.join(BASE_DIR, "media")
STATIC_DIR = os.path.join(BASE_DIR, "static")

LOG_DIR = os.path.join(BASE_DIR, "logs")
LOG_FILE = os.path.join(LOG_DIR, "app.log")
LOG_LEVEL = logging.WARNING
LOG_BACKUP_DAYS = 7
LOG_CONSOLE = True
LOG_CONSOLE_COLOR = True

TEMPLATE_DIR = os.path.join(BASE_DIR, "app", "views")

HOST = "127.0.0.1"
PORT = 8080
DEBUG = True
RELOADER = True
