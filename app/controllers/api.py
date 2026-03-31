import json

from bottle import response

from app import app, validate_csrf_token


@app.get("/api/ping")
def ping():
    response.content_type = "application/json"
    return json.dumps({"status": "ok"})



@app.post("/api/protected")
def protected():
    validate_csrf_token()

    response.content_type = "application/json"
    return json.dumps({"status": "protected-ok"})
