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
            "Author": self.name,
            "Created at":
            '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
        }
        User.commentid += 1
        comment_data.append(my_comment)
        print(comment_data)

    def edit_comment(self, commid, comment_update, status):
        self.commentid = commid
        self.comment_update = comment_update
        self.status = status

        edit_this = [comm for comm in comment_data if comm['ID'] == commid]
        if len(edit_this) == 0:
            return {'message': 'No comment  found'}
        else:
            if status == "admin" or "moderator":
                comment_data[0]["Comment"] = comment_update
                entry = [
                    entry for entry in comment_data if entry['ID'] == commid
                ]
                comment_data.remove(entry[0])
        print(comment_data)

    def moderator_roles(self, status):
        self.status = status
        if status == "moderator":
            print("You can delete any comment")

    def delete_comment(self, commitid, status):
        self.commentid = commitid
        edit_this = [comm for comm in comment_data if comm['ID'] == commitid]
        if len(edit_this) == 0:
            return {'message': 'No comment  found'}
        else:
            if status == "admin":
                entry = [
                    entry for entry in comment_data if entry['ID'] == commitid
                ]
                comment_data.remove(entry[0])
                print("successfully deleted")
            else:
                print("You must be admin to delete")


james = User("james", "james@example.com", "its-secret", "admin")
james.create_user()
james.login()
james.comment("THis is my comment")
james.edit_comment(0, "Edit me", "admin")
james.delete_comment(0, "admin")
