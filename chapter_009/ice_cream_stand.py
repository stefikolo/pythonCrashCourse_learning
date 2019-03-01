from chapter_009.restaurant import Restaurant


class IceCreamStand(Restaurant):

    def __init__(self, name, cuisine_type):
        super().__init__(name, cuisine_type)
        self.flavours = ['vanilla', 'chocolate', 'strawberry', 'fruit sorbet', 'salty caramel']

    def display_available_flavours(self):
        print('Currently available flavours: ')
        for flavour in self.flavours:
            print(f'- {flavour}')


if __name__ == '__main__':
    ice_cream = IceCreamStand('Milk it!', 'ice cream')
    ice_cream.describe_restaurant()
    ice_cream.increment_number_served(2)
    print(ice_cream.number_served)
    ice_cream.display_available_flavours()
