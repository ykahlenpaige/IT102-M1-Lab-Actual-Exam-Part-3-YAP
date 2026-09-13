import json
import os


USERS_FILE = "users.json"
SAVES_FILE = "game_saves.json"


def load_users():
    if not os.path.exists(USERS_FILE):
        return {}

    with open(USERS_FILE, "r") as file:
        return json.load(file)


def save_user(username, password):
    users = load_users()

    users[username] = {
        "password": password
    }

    with open(USERS_FILE, "w") as file:
        json.dump(users, file, indent=4)


def user_exists(username):
    users = load_users()
    return username in users


def find_user(username):
    users = load_users()
    return users.get(username)


def load_saves():
    if not os.path.exists(SAVES_FILE):
        return {}

    with open(SAVES_FILE, "r") as file:
        return json.load(file)


def save_game(username, progress):
    saves = load_saves()
    saves[username] = progress

    with open(SAVES_FILE, "w") as file:
        json.dump(saves, file, indent=4)


def get_save(username):
    saves = load_saves()
    return saves.get(username)
