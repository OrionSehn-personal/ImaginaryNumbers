import numpy as np

'''-----------------------------------------------------------------------------
Complex Number Module
Made to represent complex numbers and their interactions. Contains a single
Class called cnum, which encapsulates a complex number in arithmetic form. 

z = a + bi where z is a complex number, a and b are real numbers and
i = sqrt(-1)

cnum stores the info of a and b, and provides several operations for which
complex numbers are defined. 


getA()
getB()
getCoords()
abs()
compliment()
argument()
__add__()
__radd__()
__sub__()
__rsub__()
__mul__()
__rmul__()
__truediv__()
__rtruediv__()




-----------------------------------------------------------------------------'''

class cnum():

    def __init__(self, a = 0, b = 0):
        self.a = a
        self.b = b

    def __repr__(self):
        return f'{self.a} + {self.b}i'

    def getA(self):
        return self.a

    def getB(self):
        return self.b

    def getCoords(self):
        return (self.a, self.b)

    def compliment(self):
        return cnum(self.a, -1 * self.b)

    def argument(self):
        return np.arctan(self.b / self.a)

    def __abs__(self):
        return np.sqrt(self.a**2 + self.b**2)

    def __add__(self, other):
        if isinstance(other, cnum):
            return cnum(self.a + other.a, self.b + other.b)
        return cnum(self.a + other, self.b)

    def __radd__(self, other):
        if isinstance(other, cnum):
            return cnum(self.a + other.a, self.b + other.b)
        return cnum(self.a + other, self.b)

    def __sub__(self, other):
        if isinstance(other, cnum):
            return cnum(self.a - other.a, self.b - other.b)
        return cnum(self.a - other, self.b)

    def __rsub__(self, other):
        if isinstance(other, cnum):
            return cnum(self.a - other.a, self.b - other.b)
        return cnum(self.a - other, self.b)

    def __mul__(self, other):
        if isinstance(other, cnum):
            return cnum((self.a * other.a) - (self.b * other.b), 
            (self.a * other.b) + (self.b * other.a))
        return cnum(self.a * other, self.b * other)

    def __rmul__(self, other):
        if isinstance(other, cnum):
            return cnum((self.a * other.a) - (self.b * other.b), 
            (self.a * other.b) + (self.b * other.a))
        return cnum(self.a * other, self.b * other)

    def __truediv__(self, other):
        if isinstance(other, cnum):
            return cnum(((self.a * other.a) + (self.b * other.b))/ (other.a**2 + other.b**2),
                         ((self.b * other.a) - (self.a * other.b))/(other.a**2 + other.b**2))
        return self /cnum(other, 0)
    
    def __rtruediv__(self, other):
        if isinstance(other, cnum):
            return cnum(((self.a * other.a) + (self.b * other.b))/ (other.a**2 + other.b**2),
                         ((self.b * other.a) - (self.a * other.b))/(other.a**2 + other.b**2))
        return self/cnum(other, 0)
    
    def test():
        testnum = cnum(1, -3)
        testnum2 = cnum(1, 2)
        print(f'{testnum}\n'
        f'Compliment: {testnum.compliment()}\n'
        f'Absolute value: {abs(testnum)} \n'
        #f'Sqrt(5) = {np.sqrt(5)}\n'
        f'Argument: {testnum.argument()}\n'
        #f'arctan(1/2) = {np.arctan(1/2)}'
        f'Add 1 and 2: {testnum + testnum2}\n'
        f'Add 1 and 2 Commutative: {5 + testnum2}\n'
        f'Subtract 1 and 2: {testnum - testnum2}\n'
        f'Subtract 1 and 2 commutative: {5 - testnum}\n'
        f'Mulitpy 1 and 2: {testnum * testnum2}\n'
        f'Mulitpy 1 and 2 Commutative: {5 * testnum2}\n' 
        f'Divide 1 and 2: {testnum / testnum2}\n'
        f'Divide 1 and 2 constant: {testnum / 10}\n'
        f'Divide 1 and 2 commutative: {10 / testnum}\n')
                                                                   

