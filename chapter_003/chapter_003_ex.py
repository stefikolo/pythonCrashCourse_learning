# ex 3.1
names = ['Piotr', 'Marcin', 'Amira']
for name in names:
    print(name)
print('\n\n')
# ex 3.2
for name in names:
    print(f"Hi, how are you {name}")
print('\n\n')
# ex 3.3
bikes = ['kross trans 11.0', 'trek', 'cannondale']
x = 0
while x < len(bikes):
    print(f"I would like to own a {bikes[x]} bike.")
    x += 1
print('\n\n')
# ex 3.4
guest_list = ['Piotr', 'Marcin', 'Amira']
for i in range(len(guest_list)):
    print(f"I want to invite you to dinner {guest_list[i]}")
print('\n\n')
# ex 3.5
print(f"Unfortunately {guest_list[-1]} will not come")
guest_list[2] = 'Adam'
for i in range(len(guest_list)):
    print(f"I want to invite you to dinner {guest_list[i]}")
print('\n\n')
# ex 3.6
print("I found bigger table so i can invite three more person")
guest_list.insert(0, 'Tomasz')
guest_list.insert(2, 'Łukasz')
guest_list.append('Michał')
for i in range(len(guest_list)):
    print(f"I want to invite you to dinner {guest_list[i]}")
print('\n\n')
# ex 3.7
print("The table will not arrive on time so i can invite only two people")
while len(guest_list) > 2:
    print(f"I'm sorry {guest_list.pop()} i can’t invite you to dinner.")

for i in range(len(guest_list)):
    print(f"I want to invite you to dinner {guest_list[i]}")

print('\n\n')

del guest_list[1]
del guest_list[0]
print(guest_list)
print('\n\n')

# ex 3.8
locations = ['tokyo', 'lisbon', 'florentia', 'krakow', 'miami']
print(locations, '\n')

print(sorted(locations), locations)
print(sorted(locations, reverse=True), locations)
locations.reverse()
print(locations)
locations.reverse()
print(locations)
locations.sort()
print(locations)
locations.sort(reverse=True)
print(locations)
print('\n\n')

# ex 3.9
new_guest_list = ['Piotr', 'Marcin', 'Amira']
print(f"I'm going to invite {len(new_guest_list)} people")

