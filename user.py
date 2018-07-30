import datetime
comment = []
users = {}


class User:
    commentid = 0

    def __init__(self, name, email, password, status):
        global comment
        global users
        self.email = email
        self.password = email
        self.name = name
        self.status = status

    def create_user(self):
        user = {self.email: {"name": self.name, "Status": self.status}}
        users.update(user)
        print(users)

    def login(self):
        today = datetime.date.today()
        print("lastLoggedInAt ", today)


james = User("james", "james@example.com", "its-secret", "normal")
james.create_user()
james.login()
