# -*- coding:utf8 -*-
from grs import Stock

class Checking(object):

    def __init__(self, data):
        self.data = data

    def ck001(self):
        mao = self.data.MAO(3, 6)
        if mao[0] > 0 and mao[1] > 0 and \
                self.data.value[-1] > 1000 and self.data.price[-1] > 10 and \
                (self.data.value[-1] > self.data.value[-2] and self.data.value[-1] > self.data.value[-3]):
            return True

        return False

    def ck002(self):
        if self.data.MA(3)[0][-1] > self.data.MA(6)[0][-1] > \
                self.data.MA(18)[0][-1] and self.data.MA(18)[1] > 0:
            return True

        return False

if __name__ == "__main__":
    checking = Checking(Stock('1215'))
    print checking.ck001()
    print checking.ck002()
