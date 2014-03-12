
import sys
import random

class Boxes(object):
    '''
    To use this script:
    >python boxes.py 5
    will execute this script with 5 different simulations
    '''

    def __init__(self, number):
        self.l = [1, 0, 0]
        self.num = number

    def remove(self):
        if self.num == 2:
            self.l.pop(1)
            self.num = 1
        else:
            self.l.pop()

    def change(self):
        if self.num == 1:
            self.num = 0
        else:
            self.num = 1

    def result(self):
        if self.l[self.num] == 1:
            return True 
        else:
            return False 

if __name__ == '__main__':
    
    N = int(sys.argv[1])

    res = {True: 0, False: 0}
    for i in xrange(N):
        box = Boxes(random.randint(0,2))
        box.remove()
        box.change()
        res[box.result()] += 1 

    print("Probability of WIN is: {0:.2f}".format(float(res[True]) / N))
