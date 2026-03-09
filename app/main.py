"""Main Flask application entry point."""

import os

from flask import Flask, jsonify, request

from app.calculator import add, divide, multiply, subtract

app = Flask(__name__)

APP_VERSION = os.environ.get("APP_VERSION", "dev")
ENVIRONMENT = os.environ.get("ENVIRONMENT", "development")


@app.route("/health")
def health():
    """Health check endpoint."""
    return jsonify(
        {
            "status": "healthy",
            "version": APP_VERSION,
            "environment": ENVIRONMENT,
        }
    )


@app.route("/calculate", methods=["POST"])
def calculate():
    """Perform a calculation based on the request body."""
    data = request.get_json(silent=True, force=True)
    if not data:
        return jsonify({"error": "Request body must be JSON"}), 400

    operation = data.get("operation")
    a = data.get("a")
    b = data.get("b")

    if operation is None or a is None or b is None:
        return jsonify({"error": "Missing required fields: operation, a, b"}), 400

    operations = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide,
    }

    if operation not in operations:
        return jsonify({"error": f"Unknown operation: {operation}"}), 400

    try:
        result = operations[operation](a, b)
        return jsonify({"result": result, "operation": operation, "a": a, "b": b})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=(ENVIRONMENT == "development"))
