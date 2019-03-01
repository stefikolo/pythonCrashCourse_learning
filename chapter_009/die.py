from random import randint


class Die:

    def __init__(self):
        self.sides = 6

    def set_sides(self, num_sides):
        self.sides = num_sides

    def roll_die(self):
        print(randint(1, self.sides))


if __name__ == '__main__':
    def_die = Die()

    ten_die = Die()
    ten_die.set_sides(10)

    twenty_die = Die()
    twenty_die.set_sides(20)

    for die in [def_die, ten_die, twenty_die]:
        for i in range(10):
            die.roll_die()
        print('next die \n')
