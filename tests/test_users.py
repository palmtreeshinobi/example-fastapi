import pytest
from app import schemas
from jose import jwt
from app.config import settings

def test_create_user(client):
    res = client.post("/users/", json={
        'email': 'jamie@rapp.com',
        'password': 'password123'
    })
    new_user = schemas.UserOut(**res.json())
    assert new_user.email == 'jamie@rapp.com'
    assert res.status_code == 201

def test_login_users(client, test_user):
    res = client.post("/login", data={
        'username': test_user['email'],
        'password': test_user['password']
    })
    login_res = schemas.Token(**res.json())
    payload = jwt.decode(login_res.access_token, settings.secret_key, algorithms=[settings.algorithm])
    id = payload.get("user_id")
    assert id == test_user['id']
    assert login_res.token_type == "bearer"
    assert res.status_code == 200

@pytest.mark.parametrize("username, password, expected_status", [
    ('jamie@rapp.com', 'wrongpass', 403),
    ('wrong@email.com', 'password123', 403),
    ('wrong@email.com', 'wrongpass', 403),
    (None, 'password123', 422),
    ('jamie@rapp.com', None, 422)
])

def test_incorrect_login(test_user, client, username, password, expected_status):
    res = client.post("/login", data={"username": username, "password": password})

    print(res.status_code)
    assert res.status_code == expected_status