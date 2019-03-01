class User:
    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname
        self.login_attempts = 0

    def desc_user(self):
        print(f'This is {self.last_name}, {self.first_name} {self.last_name}')

    def greet(self):
        print(f"hello {self.first_name}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Admin(User):

    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.privilages = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print(self.privilages)


if __name__ == '__main__':
    pawel = User('Paweł', 'Bejtka')
    pawel.desc_user()
    pawel.greet()

    admin = Admin('admin', 'admin')
    admin.desc_user()
    admin.show_privileges()
