import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from webtest import TestApp

from config import CSRF_COOKIE_NAME, CSRF_FORM_FIELD
from app import app  # noqa: E402
from app import log  # noqa: F401, E402
from app.controllers import api, html, static  # noqa: F401, E402


test_app = TestApp(app)


def _extract_cookie_value(set_cookie_header: str, cookie_name: str) -> str:
    match = re.search(rf"{re.escape(cookie_name)}=([^;]+)", set_cookie_header)
    assert match, f"Cookie {cookie_name} not found in Set-Cookie header"
    return match.group(1)


def test_ping():
    resp = test_app.get("/api/ping")
    assert resp.content_type.startswith("application/json")
    assert json.loads(resp.text) == {"status": "ok"}


def test_protected_requires_csrf():
    resp = test_app.post("/api/protected", {}, status=403)
    assert resp.status_int == 403


def test_protected_accepts_valid_csrf():
    get_resp = test_app.get("/")
    set_cookie = get_resp.headers.get("Set-Cookie", "")

    csrf_token = _extract_cookie_value(set_cookie, CSRF_COOKIE_NAME)

    resp = test_app.post("/api/protected", {CSRF_FORM_FIELD: csrf_token})
    assert resp.status_int == 200
    assert json.loads(resp.text) == {"status": "protected-ok"}

