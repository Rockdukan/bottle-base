from app import app, log as _log  # noqa: F401
from app.controllers import api as _api, html as _html, static as _static  # noqa: F401
from config import HOST, PORT, DEBUG, RELOADER


if __name__ == "__main__":
    app.run(
        host=HOST,
        port=PORT,
        debug=DEBUG,
        reloader=RELOADER,
    )
