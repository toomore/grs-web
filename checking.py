# -*- coding:utf8 -*-
from grs import BestFourPoint
from grs import Stock
from numpy import std

class Checking(object):

    def __init__(self, data):
        self.data = data

    def ck001(self):
        ''' 3-6負乖離且向上，三日內最大量，成交量大於 1000 張，
            收盤價大於 10 元。（較嚴謹的選股）'''
        mao = self.data.MAO(3, 6)
        if mao[0] > 0 and mao[1] > 0 and \
                self.data.value[-1] > 1000 and self.data.price[-1] > 10 and \
                max(self.data.value[-3:]) == self.data.value[-1]:
            return True

        return False

    def ck002(self):
        ''' 3日均價大於6日均價，6日均價大於18日均價。
           （短中長線呈現多頭的態勢）'''
        ma_18 = self.data.MA(18)

        if self.data.MA(3)[0][-1] > self.data.MA(6)[0][-1] > ma_18[0][-1] and \
                ma_18[1] > 0:
            return True

        return False

    def ck003(self):
        ''' 當日成交量，大於前三天的總成交量。（短線多空動能）'''
        value = self.data.value
        if value[-1] > sum(value[-4:-1]):
            return True

        return False

    def ck004(self):
        ''' 價走平一個半月。（箱型整理、盤整）'''
        if std(self.data.price[-45:]) < 0.25:
            return True

        return False

    def ck005(self):
        ''' 判斷四大買賣點 '''
        result = BestFourPoint(self.data).best_four_point()
        if result:
            if result[0]:
                return u'buy: %s' % result[1]
            else:
                return u'sell: %s' % result[1]
        else:
            return u'Do nothing.'

if __name__ == "__main__":
    checking = Checking(Stock('2377'))
    print u'%s %s' % checking.data.info
    print checking.ck001()
    print checking.ck002()
    print checking.ck003()
    print checking.ck004()
    print checking.ck005()
