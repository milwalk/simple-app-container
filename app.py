import os

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/health-check", methods=["GET"])
def health_check():
    return jsonify({"status": "ok"}), 200


@app.route("/hello-world", methods=["GET"])
def hello_world():
    message = os.getenv("SERVER_HELLO", "Hello from app.py")
    return message, 200, {"Content-Type": "text/plain; charset=utf-8"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False)
