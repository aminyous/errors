class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        raise NotImplementedError("This feature has not been implemented yet.")


client = User("Amine", "123")
client.login()

