# Create a package named as you
# Create a file for basic Math ops
# Create the following pi, e, round, trunc, ceil

import math

class myMaths():    

    def __init__(self) -> None:
        self.myPi = math.pi
        self.myE = math.e

    def get_pi(self):
        print(f'The value of PI is: {self.myPi}')
        return math.pi

    def get_e(self):
        print(f'The value of e is: {math.e}')
        return math.e

    def round_my_num(self, my_num):
        self.mycalc = round(my_num,2)
        print(f'The value of Round is: {self.mycalc}')
        return self.mycalc

    def trunc_my_num(self, my_num):
        self.mycalc = math.trunc(my_num)
        print(f'The value of Trunc is: {self.mycalc}')
        return self.mycalc

    def ceil_my_num(self, my_num):
        self.mycalc = math.ceil(my_num)
        print(f'The value of Trunc is: {self.mycalc}')
        return self.mycalc


