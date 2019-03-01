from chapter_009.user import User
from chapter_009.privilages import Privilages


class Admin(User):

    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.privilages = Privilages()


if __name__ == '__main__':
    admin = Admin('admin', 'admin')
    admin.desc_user()
    admin.privilages.show_privileges()
