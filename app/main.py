from flask import Flask, jsonify
import logging
from datetime import datetime
import os
import time

app = Flask(__name__)

# logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

start_time = time.time() 


@app.route("/health", methods=["GET"])
def health():
    logging.info("Health check requested")
    return jsonify({
        "status": "ok",
        "service": "devops-demo",
        "timestamp": datetime.utcnow().isoformat()
    }), 200


@app.route("/status", methods=["GET"])
def status():
    uptime = int(time.time() - start_time)
    env = os.getenv("ENVIRONMENT", "local")

    logging.info("Status requested")

    return jsonify({
        "service": "devops-demo",
        "uptime_seconds": uptime,
        "environment": env
    }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
