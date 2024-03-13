'''
Course: 1P10
Author: Allen(Zifeng) An
student#: 400114057 MACID: anz8
Date: Mar.2.2018
This is a game for the bonus activity
'''
# import library
from random import randint
import time


class Map(object):
    def __init__(self):
        # initialize variables
        self.width = 5
        self.length = 4
        self.map_list = list(range(self.width))
        self.keep_running = True
        for i in range(self.width):  # 2D list
            self.map_list[i] = [0] * self.length
        # generating mines
        self.mine_number = 3
        self.flag_number = self.mine_number
        print('There will be ' + str(self.mine_number) + ' mine(s) in this game!')
        self.mine_list = list(range(self.mine_number))
        for i in range(self.mine_number):
            mine_coordinate = [randint(0, self.width - 1), randint(0, self.length - 1)]
            while mine_coordinate in self.mine_list:
                mine_coordinate = [randint(0, self.width - 1), randint(0, self.length - 1)]
            self.mine_list[i] = mine_coordinate
            self.map_list[mine_coordinate[0]][mine_coordinate[1]] = -10  # a negative number is a mine

    def numbered_map(self):  # create a map with numbers
        for i in range(self.mine_number):
            x = self.mine_list[i][0]
            y = self.mine_list[i][1]
            self.left = x - 1 >= 0
            self.down = y + 1 < self.length
            self.up = y - 1 >= 0
            self.right = x + 1 < self.width
            if self.left:
                self.map_list[x - 1][y] += 1
            if self.left and self.up:
                self.map_list[x - 1][y - 1] += 1
            if self.left and self.down:
                self.map_list[x - 1][y + 1] += 1
            if self.right:
                self.map_list[x + 1][y] += 1
            if self.right and self.up:
                self.map_list[x + 1][y - 1] += 1
            if self.right and self.down:
                self.map_list[x + 1][y + 1] += 1
            if self.up:
                self.map_list[x][y - 1] += 1
            if self.down:
                self.map_list[x][y + 1] += 1
        for y in range(self.length):  # convert the negative number to the mine
            for x in range(self.width):
                if self.map_list[x][y] < 0:
                    self.map_list[x][y] = '*'

    def visibility(self):  # create another map of booleans to decide if the numbers are revealed
        self.visibility_list = list(range(self.width))
        for i in range(self.width):  # 2D list
            self.visibility_list[i] = [False] * self.length

    def output(self):
        print('You have ' + str(self.flag_number) + ' flag(s) left!')
        for y in range(self.length):
            for x in range(self.width):
                if self.visibility_list[x][y] == False:
                    print('?', end=' ')
                elif self.visibility_list[x][y] == True:
                    print(self.map_list[x][y], end=' ')
                elif self.visibility_list[x][y] == 'flagged':
                    print('>', end=' ')
            print("")
        print('')

        # for y in range(self.length):  # the commented code can reveal the underlying map with mines and numbers
        #     for x in range(self.width):
        #         print(self.map_list[x][y], end=' ')
        #     print("")

    def user_numinput(self):
        while True:
            try:
                choice_num = int(input('Choose 1.Flag 2.Left click 3.Remove flag. Please enter either 1 or 2 or 3: '))
                if choice_num == 1 or choice_num == 2 or choice_num == 3:
                    break
                else:
                    print('Invalid entry')
            except:
                print('Invalid entry')
        return choice_num

    def user_coordinate_input(self):
        while True:
            try:
                coordinate = input('Please enter the coordinates in the form of x,y: ')
                temp = coordinate.split(',')
                if int(temp[0]) < self.width and int(temp[1]) < self.length and int(temp[0]) >= 0 and int(temp[1]) >= 0:
                    break
                else:
                    print('Invalid entry')
            except:
                print('Invalid entry')
        return coordinate

    def user_click(self):
        counter = 0
        self.keep_running = True
        for truth_list in self.visibility_list:
            if False in truth_list:
                counter += 1
        if counter == 0:
            self.keep_running = False

        if self.keep_running:
            self.choice = self.user_numinput()
            self.clicking = self.user_coordinate_input()
            temp = self.clicking.split(',')
            x = int(temp[0])
            y = int(temp[1])
            if self.choice == 1:  # flag
                self.flag_number -= 1
                if self.flag_number < 0:
                    print('You have used all of the flags!')
                    return self.user_click()
                else:
                    self.visibility_list[x][y] = 'flagged'
                    self.output()
                    return self.user_click()
            elif self.choice == 2:  # right click
                if self.visibility_list[x][y] == 'flagged':
                    print('Remove the flag first before right clicking!')
                    return self.user_click()
                if [x, y] in self.mine_list:
                    for i in self.mine_list:
                        self.visibility_list[i[0]][i[1]] = True
                    self.output()
                    time.sleep(0.4)
                    for y in range(self.length):
                        for x in range(self.width):
                            print(self.map_list[x][y], end=' ')
                        print("")
                    quit('Blast!You DIE')
                else:
                    self.expand(x, y)
                    self.output()
                return self.user_click()
            elif self.choice == 3:  # remove flag
                if self.visibility_list[x][y] == 'flagged':
                    self.flag_number += 1
                    self.visibility_list[x][y] = False
                    self.output()
                    return self.user_click()
                else:
                    print('You cannot remove a flag where there is no flag!')
                    return self.user_click()

        else:
            time.sleep(0.4)
            quit("Mission accomplished! You Won!")

    # when the user click on a unit that does not have a mine, it will expand until a number is found
    def expand(self, x, y):
        if self.map_list[x][y] != 0:
            self.visibility_list[x][y] = True

        elif self.map_list[x][y] == 0:
            self.visibility_list[x][y] = True
            if x - 1 >= 0 and self.visibility_list[x - 1][y] == False:
                self.expand(x - 1, y)
            if x + 1 < self.width and self.visibility_list[x + 1][y] == False:
                self.expand(x + 1, y)
            if y - 1 >= 0 and self.visibility_list[x][y - 1] == False:
                self.expand(x, y - 1)
            if y + 1 < self.length and self.visibility_list[x][y + 1] == False:
                self.expand(x, y + 1)
            if x - 1 >= 0 and y - 1 >= 0 and self.visibility_list[x - 1][y - 1] == False:
                self.expand(x - 1, y - 1)
            if x + 1 < self.width and y - 1 >= 0 and self.visibility_list[x + 1][y - 1] == False:
                self.expand(x + 1, y - 1)
            if x - 1 >= 0 and y + 1 < self.length and self.visibility_list[x - 1][y + 1] == False:
                self.expand(x - 1, y + 1)
            if x + 1 < self.width and y + 1 < self.length and self.visibility_list[x + 1][y + 1] == False:
                self.expand(x + 1, y + 1)


def main():
    testing = Map()
    testing.numbered_map()
    testing.visibility()
    testing.output()
    testing.user_click()


print('You were knocked out by a mafia and he hooked you up to a machine in the hospital.\n'
      'The machine threw you into a virtual reality and now you woke up in the middle of nowhere.\n'
      'You examined your surroundings carefully and you think you are on the boarder of North and South Korea\n'
      'Based on the number of dead bodies beside you, you realize this is a mine field that was created 50 years ago.\n'
      'The coordinate starts with the top left mine (0,0). When you go right 1 unit, x coordinate plus 1.\n'
      'When you go down 1 unit, y coordinate plus 1.\nGOOD LUCK!\n')

main()
