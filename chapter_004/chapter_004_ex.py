# ex 4.1
pizza_types = ['pepperoni', 'hawaii', 'margarita']
for kind in pizza_types:
    print(kind)
print('\n\n')

for kind in pizza_types:
    print(f"I like {kind} pizza")
print('\n\n')

# ex 4.2
animal_list = ['dog', 'fox', 'wolf']
for animal in animal_list:
    print(f"{animal} would be a great pet")

print(f"{animal_list[0]}, {animal_list[1]} "
      f"and {animal_list[2]} are all from feline family")
print('\n\n')

# ex 4.3
for i in range(1, 21):
    print(i)

# ex 4.4
milion_digit_list = list(range(1, 1000001))
print(milion_digit_list)

# ex 4.5
print(min(milion_digit_list), max(milion_digit_list), sum(milion_digit_list))


# ex 4.6
for i in range(1, 21, 2):
    print(i)

# ex 4.7
threes_list = [x for x in range(3, 31) if x % 3 == 0]
for num in threes_list:
    print(num)


# ex 4.8
cubes_list = [x ** 3 for x in range(1, 11)]
for num in cubes_list:
    print(num)

# ex 4.10
print(f"First three digits of threes_list are: {threes_list[:3]}")
print(f"Middle three digits of milion_digit_list are: {milion_digit_list[1500:1503]}")
print(f"Last three digits of cubes_list are: {cubes_list[-3:]}")

# ex 4.11
friend_pizzas = pizza_types[:]
friend_pizzas.append('carbonara')
pizza_types.append('diavolo')
print(friend_pizzas, pizza_types)
# ex 4.13
# TODO exercise from tuples page 71
