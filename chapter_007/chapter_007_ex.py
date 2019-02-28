# 7.1
def car():
    what_car_input = input('What car do you want to rent? ')
    print(f'Let me see if i can find you a {what_car_input}')

# 7.2
def guests():
    how_many_guests_input = int(input('how many people are in the group? '))
    if how_many_guests_input > 8:
        print(f'you will have to wait')
    else:
        print('let me show you the table')

# 7.3
def by_ten():
    num_test = int(input('type some number -> '))
    print(f'{num_test} is multiple of 10') if num_test % 10 == 0 else print(f'{num_test} is not multiple of 10')

# 7.4
flag = True

while flag:
    user_top = input('What pizza topping do you want? (type quit to finish) ')
    if user_top == 'quit':
        flag = False
    else:
        print(f'{user_top} is added to your pizza order')

# 7.5
user_age = int(input('How old are you'))
if user_age < 3:
    print('the ticket is: free')
elif user_age < 12:
    print('the ticket is: $10')
else:
    print('the ticket is: $15')

# 7.6
i = 2
while i > 0:
    print('loop')
    i -= 1

# 7.7
# infinite loop

# 7.8 # 7.9
sandwich_orders = ['ham', 'pastrami','egg', 'burger', 'pastrami', 'cheese', 'tuna', 'pastrami']
finished_sandwiches = []
print('we run out of pastrami!')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    sand = sandwich_orders.pop()
    print(f'I made your {sand} sandwich')
    finished_sandwiches.append(sand)
print(finished_sandwiches)
