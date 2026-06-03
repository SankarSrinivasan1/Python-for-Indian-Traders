def save_access_token(token):
    with open("token.txt", "w") as file:
        file.write(token)
