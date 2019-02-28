# 5.1
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

# 5.2
print('milk' == 'salad')
print('Milk'.lower() == 'milK'.lower())
print(2 == (16//8))
print(3 >= 2)
print(5 <= 5)
print(6 > 3)
print(2 == 2 and 4 //2 == 2)
print(64 == 2 or 'life' == 'life')
print('b' in ['a', 'b', 'c'])
print('b' not in ['a', 'b', 'c'])

# 5.3
alien_color = 'yellow'
if alien_color == 'green':
    print('you earned 5 points!')

# 5.4
else:
    print('you earned 10 points!')

# 5.5
alien_color = 'yellow'
if alien_color == 'green':
    print('you earned 5 points!')
elif alien_color == 'red':
    print('you earned 15 points!')
else:
    print('you earned 10 points!')

# 5.6
age = 7
if age < 2:
    print('you are a baby!')
elif age < 4:
    print('you are a toddler!')
elif age < 13:
    print('you are a kid!')
elif age < 20:
    print('you are a teen!')
elif age < 65:
    print('you are an adult!')
else:
    print('you are an elder!')

# 5.7
fav_fruits = ['apple', 'banana', 'cherry']
fruit = 'banana'
if fruit in fav_fruits:
    print(f'hey, you really like {fruit}')

# 5.8, 5.9
user_names = ['a', 'b', 'admin', 'd', 'de']
if len(user_names) < 1:
    print("we need to find some users")
else:
    for user in user_names:
        if user == 'admin':
            print(f'Hello {user}, here are the reports!')
        else:
            print(f'Hello {user}, welcome back!')

# 5.10
curr_users = ['a', 'b', 'admin', 'D', 'de']
new_users = ['A', 'bfg', 'ghtfyj', 'd', 'degjtyhs']
curren_lower = [x.lower() for x in curr_users]
for nuser in new_users:
    if nuser.lower() in curren_lower:
        print(f"This name '{nuser}' is already taken")
    else:
        print(f'New user with username: {nuser} successfully created')

# 5.11
ten_nums = [x for x in range(1, 10)]
for num in ten_nums:
    if num == 1:
        print(f'cardinal: {num}, ordinal: {num}st')
    elif num == 2:
        print(f'cardinal: {num}, ordinal: {num}nd')
    elif num == 3:
        print(f'cardinal: {num}, ordinal: {num}rd')
    else:
        print(f'cardinal: {num}, ordinal: {num}th')

