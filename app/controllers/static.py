from bottle import static_file

from app import app
from config import MEDIA_DIR, STATIC_DIR


@app.get(r"/media/<filepath:path>")
def media(filepath):
    return static_file(filepath, root=MEDIA_DIR)


@app.get(r"/static/css/<filepath:re:.*\.css>")
def css(filepath):
    return static_file(filepath, root=os.path.join(STATIC_DIR, "css"))


@app.get(r"/static/fonts/<filepath:re:.*\.(eot|otf|svg|ttf|woff|woff2?)>")
def font(filepath):
    return static_file(filepath, root=os.path.join(STATIC_DIR, "fonts"))


@app.get(r"/static/img/<filepath:re:.*\.(jpg|png|gif|ico|svg)>")
def img(filepath):
    return static_file(filepath, root=os.path.join(STATIC_DIR, "img"))


@app.get(r"/static/js/<filepath:re:.*\.(js|json)>")
def js(filepath):
    return static_file(filepath, root=os.path.join(STATIC_DIR, "js"))
