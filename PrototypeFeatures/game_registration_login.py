import save_files


def register(username, password):
    username = username.strip()

    if username == "":
        return False, "Please enter a username."

    if password == "":
        return False, "Please enter a password."

    if save_files.user_exists(username):
        return False, "Username already exists."

    save_files.save_user(username, password)

    return True, "Registration successful."


def login(username, password):
    username = username.strip()

    user = save_files.find_user(username)

    if user is None:
        return False, "Account not found."

    if user["password"] != password:
        return False, "Incorrect password."

    return True, "Login successful."
