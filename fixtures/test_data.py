import pytest

class LoginTestData:
    VALID_USERS = [
        {"username": "user1", "password": "pass1", "role": "admin"},
        {"username": "user2", "password": "pass2", "role": "user"}

    ]

    INVALID_USERS = [
        {"username": "wrong", "password": "wrong", "expected_error": "Invalid credentials"},
        {"username": "user1", "password": "", "expected_error": "Password is required"}

    ]

@pytest.fixture(params=LoginTestData.VALID_USERS)
def valid_user(request):
    return request.param

@pytest.fixture(params=LoginTestData.INVALID_USERS)
def invalid_user(request):
    return request.param