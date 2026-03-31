from bottle import template

from app import app, generate_csrf_token
from config import CSRF_FORM_FIELD


@app.route("/")
def index():
    csrf_token = generate_csrf_token()

    return template(
        "index",
        csrf_form_field=CSRF_FORM_FIELD,
        csrf_token=csrf_token,
        name="Bottle",
    )
