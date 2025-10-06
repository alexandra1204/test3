import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from register import register, USERS

@pytest.mark.parametrize("username,password,email,expected_status", [
    ("user1", "pass123", "user1@example.com", "success"),
    ("user2", "pass456", "user2@example.com", "success"),
    ("", "pass", "user@example.com", "error"),
    ("user3", "", "user3@example.com", "error"),
    ("user4", "pass", "", "error"),
    ("user1", "pass789", "user1@example.com", "error"),  
    ("user5", "pass", "invalidemail", "error")
])
def test_register(username, password, email, expected_status):
    result = register(username, password, email)
    assert result["status"] == expected_status
