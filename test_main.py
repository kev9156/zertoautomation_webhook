from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_zerto_webhook():
    # Test the API call
    response = client.post("/zerto", json={"vpgName": "Automation_Test"})
    
    # Assert the immediate response
    assert response.status_code == 200
    assert response.json() == {"status": "accepted", "target_vpg": "Automation_Test"}