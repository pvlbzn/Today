# Operator overloading and magic methods exercise

from math import hypot


class Vector:
    def __init__(self, x, y):
        '''
        Initialization
        '''
        self.x = x
        self.y = y

    def __repr__(self):
        '''
        String representation
        '''
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        '''
        Absolute value
        '''
        return hypot(self.x, self.y)

    def __bool__(self):
        '''
        Boolean representation
        '''
        return bool(abs(self))

    def __add__(self, second):
        '''
        Addition operator overloading
        '''
        return Vector(self.x + second.x, self.y + second.y)

    def __mul__(self, scalar):
        '''
        Multiplication overloading
        '''
        return Vector(self.x * scalar, self.y * scalar)
