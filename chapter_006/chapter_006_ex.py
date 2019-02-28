# 6.1 # 6.11
people = {
    'Ola': {
        'name': 'ola',
        'surname': 'tomala',
        'age': 28,
        'city': 'Warsaw'
    },
    'Paweł': {
        'name': 'paweł',
        'surname': 'bejtka',
        'age': 27,
        'city': 'Warsaw'
    }
}
for person, data in people.items():
    print(f'{person}:')
    for item in data.keys():
        print(f'{item}: {data[item]}')
    print('\n')

# 6.2/6.3
fav_num = {'Ola': 7,
           'Mariusz': 44,
           'Tomek': 11,
           'Maciej': 75,
           'Franek': 44,
           'Benny': 44}
for key, value in fav_num.items():
    print(f'{key} fav number is {value}')
print('\n')

for key in set(sorted(fav_num.values())):
    print(f'{key} fav number is')
print('\n')

# 6.4 # 6.5
maj_rivers = {
    'nile': 'egypt',
    'amazonka': 'brasil',
    'vistula': 'poland'
}
for river in maj_rivers.keys():
    print(river.title())
for country in maj_rivers.values():
    print(country.title())

# 6.6
people_to_poll = ['Krzychu', 'Mariusz', 'Ola', 'Marcin', 'Piotr']
for name in people_to_poll:
    if name in fav_num.keys():
        print(f'Thank you for filling the poll {name}!')
    else:
        print(f'Hi {name}, please take part in my poll!')

# 6.7 # 6.8

Ola = {
    'name': 'ola',
    'surname': 'tomala',
    'age': 28,
    'city': 'Warsaw'
}
Pawel = {
    'name': 'paweł',
    'surname': 'bejtka',
    'age': 27,
    'city': 'Warsaw'
}
people_list = [Ola, Pawel]
print(len(people_list))
for person in people_list:
    print(person)
    print(person['age'])

# 6.9 # 6.10
fav_places = {'Ola': ['lisbon', 'barcelona', 'umia'],
              'Mariusz': ['warszawa', 'gdansk', 'kolobrzeg']}

for name in fav_places.keys():
    print(f'{name} fav places are:')
    for place in fav_places[name]:
        print(f'- {place}')

# 6.12
