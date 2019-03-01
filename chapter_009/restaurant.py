class Restaurant:

    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f'{self.name} restaurant offers {self.cuisine_type} cuisine')

    def open_restaurant(self):
        print('restaurant is open')

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, num_served):
        self.number_served += num_served


if __name__ == '__main__':
    greek_restaurant = Restaurant('Zorba', 'greek and balkan food')
    print(greek_restaurant.name, greek_restaurant.cuisine_type)
    print(greek_restaurant.describe_restaurant())
    print(greek_restaurant.open_restaurant())

