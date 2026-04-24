from fastapi.testclient import TestClient
from unittest.mock import MagicMock
import main

client = TestClient(main.app)


def test_create_job():
    main.r = MagicMock()
    response = client.post("/jobs")
    assert response.status_code == 200
    assert "job_id" in response.json()


def test_get_job_found():
    main.r = MagicMock()
    main.r.hget.return_value = b"completed"

    response = client.get("/jobs/test123")
    assert response.status_code == 200
    assert response.json()["status"] == "completed"


def test_get_job_not_found():
    main.r = MagicMock()
    main.r.hget.return_value = None

    response = client.get("/jobs/test123")
    assert response.status_code == 200
    assert response.json()["error"] == "not found"
