file = './files/notes.txt'
wfile = './files/guests.txt'

with open(file, 'r') as my_file:
    a = my_file.read()

print(a)

with open(file, 'r') as my_file:
    for line in my_file:
        print(line)

with open(file, 'r') as my_file:
    line_list = my_file.readlines()

print(type(line_list), line_list)


def add_guest():
    guest = input('Type your name here: ')
    with open(wfile, 'a') as guest_book:
        guest_book.write(f'{guest}\n')


try:
    int_in = int(input('type a number '))
except ValueError:
    print('provided input is not a number')
else:
    print(int_in)


if __name__ == '__main__':
    add_guest()
