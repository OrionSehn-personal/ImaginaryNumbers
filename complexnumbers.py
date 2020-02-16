from math import *

'''-----------------------------------------------------------------------------
Complex Number Module
Made to represent complex numbers and their interactions. Contains a single
Class called cnum, which encapsulates a complex number in arithmetic form. 

z = a + bi where z is a complex number, a and b are real numbers and
i = sqrt(-1)

cnum stores the info of a and b, and provides several operations for which
complex numbers are defined. 

abs()
__add__
__sub__
__mul__
__truediv__
__floordiv__
__lt__
__le__
__gr__
__ge__
__ne__
polar()
compliment



-----------------------------------------------------------------------------'''

class cnum(a, b):
    self.a = 0
    self.b = 0
    def __init__(self, a = 0, b = 0):
        self.a = a
        self.b = b

    def __abs__(self):
        return sqrt(self.a + self.b)

    def __add__(self, other):
        if isinstance(other, cnum):
            return cnum(self.a + other.a, self.b, other.b)
        return cnum(self.a + other, self.b)

    def __sub__(self, other):
        if isinstance(other, cnum):
            return cnum(self.a - other.a, self.b, other.b)
        return cnum(self.a - other, self.b)


    def __mul__(self, other):
        if isinstance(other, cnum):
            return cnum((self.a * other.a) - (self.b * other.b), 
            (self.a * other.b) + (self.b * other.a))
        return cnum(other * self.a, other * self.b)

    def __pow__(self, other):
        if isinstance(other, int) != True:
            AssertionError("exponent must be an integer value")


    def __truediv__(self, other)):
        if isinstance(other, cnum):
            return (abs(other) * abs(other)) * (self * other.compliment())
        return 

    def __floordiv__(self, other)):
    def __lt__(self, other)):
    def __le__(self, other)):
    def __gr__(self, other)):
    def __ge__(self, other)):
    def __ne__(self, other)):
    def polar():
        pass
    def compliment():
        return cnum(self.a, -1 * self.b)




