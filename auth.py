# auth.py
import hashlib

# Простая имитация базы пользователей
USERS = {
    "admin": hashlib.sha256("1234".encode()).hexdigest(),
    "qa_user": hashlib.sha256("password".encode()).hexdigest()
}


def login(username: str, password: str) -> dict:
    """
    Функция логина. Возвращает словарь со статусом и токеном, если всё корректно.
    """
    if not username or not password:
        return {"status": "error", "message": "Username and password required"}

    hashed_pw = hashlib.sha256(password.encode()).hexdigest()

    if username in USERS and USERS[username] == hashed_pw:
        token = hashlib.sha256(f"{username}:{password}".encode()).hexdigest()
        return {"status": "success", "token": token}

    return {"status": "error", "message": "Invalid credentials"}


def logout(token: str) -> dict:
    """
    Имитация выхода из системы.
    """
    if not token:
        return {"status": "error", "message": "Token required"}
    return {"status": "success", "message": "Logged out"}
