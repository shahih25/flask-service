users = []

def add_user(username, password):
    users.append({ "username": username, "password": password })
    return ''


def get_user_by_username(username):
    for user in users:
        if user["username"] == username:
            return user
    
    return None


def update_password(username, new_password):
    print(username + new_password)
    for user in users:
        print(user)
        if user["username"] == username:
            user["password"] = new_password
            return ''
    
    return None


def delete_user(username):
    for user in users:
        if user["username"] == username:
            users.remove(user)
            return ''
        
    return None
