import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get():
    r = requests.get(f"{BASE_URL}/users/3")
    assert r.status_code == 200
    data = r.json()
    for key in ("id", "name", "username", "email", "address", "phone", "website", "company"):
        assert key in data

def test_post():
    payload = {
        "name": "MashaTest",
        "username": "test_user",
        "email": "masha@test.com"
    }
    r = requests.post(f"{BASE_URL}/users", json=payload)
    assert r.status_code == 201
    assert "id" in r.json()

def test_put():
    payload = {
        "id": 3,
        "name": "Updated Masha",
        "username": "updated_test_user",
        "email": "masha_updated@test.com"
    }
    r = requests.put(f"{BASE_URL}/users/3", json=payload)
    assert r.status_code == 200
    data = r.json()
    assert data["name"] == payload["name"]
