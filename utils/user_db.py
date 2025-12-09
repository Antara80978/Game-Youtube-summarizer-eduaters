import json
import os

USER_DB_PATH = "user_data.json"

# Initialize the DB file if not exists
if not os.path.exists(USER_DB_PATH):
    with open(USER_DB_PATH, "w") as f:
        json.dump({}, f)

def register_user(username, password):
    with open(USER_DB_PATH, "r") as f:
        users = json.load(f)

    if username in users:
        return False

    users[username] = {"password": password, "points": 0}

    with open(USER_DB_PATH, "w") as f:
        json.dump(users, f)

    return True

def check_user(username, password):
    with open(USER_DB_PATH, "r") as f:
        users = json.load(f)

    return username in users and users[username]["password"] == password

def get_points(username):
    with open(USER_DB_PATH, "r") as f:
        users = json.load(f)
    return users.get(username, {}).get("points", 0)

def update_points(username, points):
    with open(USER_DB_PATH, "r") as f:
        users = json.load(f)

    if username in users:
        users[username]["points"] += points

        with open(USER_DB_PATH, "w") as f:
            json.dump(users, f)
