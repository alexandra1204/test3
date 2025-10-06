import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from auth import login, logout
import pytest


@pytest.mark.parametrize("username,password,expected", [
    ("admin", "1234", "success"),
    ("qa_user", "password", "success"),
    ("admin", "wrong", "error"),
    ("", "1234", "error"),
    ("admin", "", "error"),
])
def test_login(username, password, expected):
    result = login(username, password)
    assert result["status"] == expected


def test_login_returns_token():
    result = login("admin", "1234")
    assert "token" in result
    assert len(result["token"]) > 10


def test_logout_success():
    login_result = login("admin", "1234")
    token = login_result["token"]
    result = logout(token)
    assert result["status"] == "success"


def test_logout_error():
    result = logout("")
    assert result["status"] == "error"
