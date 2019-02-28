# 8.1
def display_message():
    print("now i'm learning about functions in python")

# 8.2
def fav_book(title):
    print(f'One of my fav books is {title}')

# 8.3 - 5
def make_shirt(size='L', slogan='I love Py'):
    print(f'your order is {size} size shirt with {slogan} printed on it')

# 8.6
def city_country(city, country):
    return f'{city}, {country}'

# 8.7
def make_album(a_name, album_title, num_of_tracks=''):
    return {'artist': a_name,'album': album_title} if num_of_tracks == '' else {'artist': a_name,'album': album_title, 'tracks_number': num_of_tracks}

# 8.8
while input('continue?(y/n) ') == 'y':
    print('enter artist name, album name and number of tracks on album')
    a_name = input('artist name: ')
    album = input('album name: ')
    tracks = input('track number: ')
    x = make_album(a_name, album, tracks)
    print(x)

# 8.9
mags = ['x', 'y', 'z']
def show_mags(mag_list):
    for mag in mag_list:
        print(mag)

# 8.10

# 8.11
def make_great(mag_list):
    for i in range(len(mag_list)):
        mag_list[i] = f'Great {mag_list[i]}'
    return mag_list

# 8.12
def sandwich_ingredients(*ings):
    print('You"ve ordered sandwich with:')
    for ing in ings:
        print(f'- {ing}')

# 8.13
def bouild_profile(fname, lname, **additional_info):
    profile = {'name': fname, 'surname': lname}
    for k, v in additional_info.items():
        profile[k] = v
    print(profile)


if __name__ == '__main__':
    display_message()
    fav_book('wiedzmin')
    make_shirt(size='s', slogan='dfberfe')
    cc_response = city_country('warsaw', 'poland')
    print(cc_response)
    ma_resp = make_album('metallica', 'black album', '11')
    print(ma_resp)
    great_mags = make_great(mags[:])
    show_mags(mags)
    show_mags(great_mags)
    sandwich_ingredients('cheese', 'butter', 'ham', 'tomato')
    bouild_profile('Mariusz', 'Majowicz', age=29, company='stepstone', jobtitle='AutomationQA')
