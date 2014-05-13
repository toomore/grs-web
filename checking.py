# -*- coding:utf8 -*-
from grs import Stock


class Checking(Stock):
    def __init__(self, no):
        super(Stock, self).__init__(no)


if __name__ == "__main__":
    checking = Checking('2618')
    print checking.MA(3)
