class User:
    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname

    def desc_user(self):
        print(f'This is {self.last_name}, {self.first_name} {self.last_name}')

    def greet(self):
        print(f"hello {self.first_name}")


if __name__ == '__main__':
    pawel = User('Paweł', 'Bejtka')
    pawel.desc_user()
    pawel.greet()
