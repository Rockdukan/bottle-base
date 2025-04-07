import json

from bottle import response

from app import app


@app.get("/api/ping")
def ping():
    response.content_type = "application/json"
    return json.dumps({"status": "ok"})
