import datetime
comment_data = []
users_data = {}


class User:
    commentid = 0

    def __init__(self, name, email, password, status):
        global comment_data
        global users_data
        self.email = email
        self.password = email
        self.name = name
        self.status = status

    def create_user(self):
        user = {self.email: {"name": self.name, "Status": self.status}}
        users_data.update(user)
        print(users_data)

    def login(self):
        today = datetime.date.today()
        print("lastLoggedInAt ", today)

    def comment(self, comment):
        self.comment = comment
        my_comment = {
            "ID": User.commentid,
            "Comment": self.comment,
            "Created by": self.name,
            "Created at":
            '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
        }
        User.commentid += 1
        comment_data.append(my_comment)
        print(comment_data)


james = User("james", "james@example.com", "its-secret", "normal")
james.create_user()
james.login()
james.comment("THis is my comment")
