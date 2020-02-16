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
    self._a = 0
    self._b = 0
    def __init__(self, a = 0, b = 0):
        self._a = a
        self._b = b
    def __abs__(self):
        return sqrt(self._a + self_b)
    def __add__( )

