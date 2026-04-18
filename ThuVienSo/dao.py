import json
import os

def auth_user(username, password):

    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "data", "users.json")

    with open(file_path, encoding="utf-8") as f:
        users = json.load(f)

    for u in users:
        if u["username"] == username and u["password"] == password:
            return True

    return False