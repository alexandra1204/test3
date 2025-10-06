
USERS = {}

def register(username: str, password: str, email: str) -> dict:
    """
    Функция регистрации нового пользователя.
    """
    if not username or not password or not email:
        return {"status": "error", "message": "All fields are required"}

    if username in USERS:
        return {"status": "error", "message": "Username already exists"}

    if "@" not in email or "." not in email:
        return {"status": "error", "message": "Invalid email"}

    USERS[username] = {"password": password, "email": email}
    return {"status": "success", "message": "User registered"}
