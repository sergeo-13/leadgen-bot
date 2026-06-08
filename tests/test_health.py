"""Tests for health check endpoint."""


def test_health_endpoint(client):
    """Test health check endpoint returns valid response."""
    response = client.get("/api/v1/health")
    assert response.status_code == 200

    data = response.json()
    assert "status" in data
    assert "postgres" in data
    assert "minio" in data
    assert data["status"] in ["ok", "degraded"]
    assert isinstance(data["postgres"], bool)
    assert isinstance(data["minio"], bool)


def test_root_endpoint(client):
    """Test root endpoint."""
    response = client.get("/")
    assert response.status_code == 200

    data = response.json()
    assert "message" in data
    assert "version" in data
    assert "docs" in data
