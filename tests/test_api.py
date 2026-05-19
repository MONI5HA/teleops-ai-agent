from fastapi.testclient import TestClient
from app.api.server import app

client = TestClient(app)

def test_query():

    response = client.post(
        "/query",
        json={
            "query": "Low SINR issue",
            "cell_id": "NR-4402"
        }
    )

    assert response.status_code == 200