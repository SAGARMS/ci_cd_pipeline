"""Integration tests for the Flask application."""

import pytest

from app.main import app


@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


class TestHealthEndpoint:
    def test_health_returns_200(self, client):
        response = client.get("/health")
        assert response.status_code == 200

    def test_health_returns_json(self, client):
        response = client.get("/health")
        data = response.get_json()
        assert data["status"] == "healthy"
        assert "version" in data
        assert "environment" in data
        assert "timestamp" in data


class TestCalculateEndpoint:
    def test_add_operation(self, client):
        response = client.post(
            "/calculate",
            json={"operation": "add", "a": 5, "b": 3},
        )
        assert response.status_code == 200
        assert response.get_json()["result"] == 8

    def test_divide_by_zero(self, client):
        response = client.post(
            "/calculate",
            json={"operation": "divide", "a": 10, "b": 0},
        )
        assert response.status_code == 400

    def test_missing_fields(self, client):
        response = client.post("/calculate", json={"operation": "add"})
        assert response.status_code == 400

    def test_unknown_operation(self, client):
        response = client.post(
            "/calculate",
            json={"operation": "modulo", "a": 10, "b": 3},
        )
        assert response.status_code == 400

    def test_no_json_body(self, client):
        response = client.post("/calculate")
        assert response.status_code == 400
