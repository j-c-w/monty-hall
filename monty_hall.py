__author__ = 'Jackson'

from random import randint

class DoorGroup():
    def __init__(self, number):
        self.number = number
        self.doors = [None] * number
        self.selected = 0
        self.doors[randint(0, number - 1)] = 1
        self.change = True

    def set_change(self, change):
        self.change = change

    def remove_random(self):
        removal = self.random_door()
        while (self.doors[removal] == 1):
            removal = self.random_door()
        del self.doors[removal]
        self.number -= 1

    def random_door(self):
        new_door = self.selected
        while new_door == self.selected:
            new_door = randint(0, self.number - 1)
        return new_door

    def select_door(self):
        self.selected = self.random_door()

    def play_turn(self):
        if self.number == 2:
            #print self.doors[self.selected] == 1
            return self.doors[self.selected] == 1
            #is the prize door
        else:
            #greater than two so keep on playing,
            self.remove_random()
            if self.change:
                self.select_door()
            return self.play_turn()

    def start(self):
        return self.play_turn()


def main():
    doors = input("Doors to use:")
    num_times = input("Number of times to simulate:")
    change_wins = 0
    stay_wins = 0
    for time in range(num_times):
        group = DoorGroup(doors)
        group.change = True
        won = group.start()
        if won:
            change_wins += 1
    for time in range(num_times):
        group = DoorGroup(doors)
        group.change = False
        won = group.start()
        if won:
            stay_wins += 1
    print "Changing wins/total = " + str(change_wins) + "/" + str(num_times) +\
          " = " + str(float(change_wins)/num_times)
    print "Staying wins/total = " + str(stay_wins) + "/" + str(num_times) +\
          " = " + str(float(stay_wins)/num_times)

main()