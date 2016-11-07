import math

class Bruch:
    def __init__(self,a,b=1):

        if(type(a)!=type(b)):
            raise TypeError
        else:
            self.zaehler=a
            self.nenner=b
            self.value=a/b

    def __invert__(self):
        temp=self.nenner
        self.nenner=self.zaehler
        self.zaehler=temp
        self.value = self.zaehler / self.nenner
        return self.value

    def __add__(self, other):
        if (type(other) != int):
            raise TypeError
        self.value+=other.value

    def __radd__(self, other):
        if (type(other) != int):
            raise TypeError
        self.value+=other.value

    def __iadd__(self, other):
        if(type(other)!=int and type(other)!=float):
            raise TypeError
        self.value+=other
        return self.value

    def __pow__(self, power, modulo=None):
        if(type(power)!=int):
            raise TypeError
        else:
            self.value= self.value**power

    def _Bruch__makeBruch(self,value):
        if(type(value)!=int and type(value)!=float):
            raise TypeError
        else:
            self.zaehler=value

    def __isub__(self, other):
        if (type(other) != int and type(other) != float):
            raise TypeError
        self.value -= other
        return self.value

    def __rsub__(self, other):
        if (type(other) != int):
            raise TypeError
        self.value-=other.value

    def __imul__(self, other):
        if (type(other) != int and type(other) != float):
            raise TypeError
        self.value *= other
        return self.value

    def __rmul__(self, other):
        if (type(other) != int):
            raise TypeError
        self.value*=other.value

    def __itruediv__(self, other):
        if (type(other) != int and type(other) != float):
            raise TypeError
        self.value /= other
        return self.value

    def __rtruediv__(self, other):
        if (type(other) != int):
            raise TypeError
        self.value/=other

    def __mul__(self, other):
        if (type(other) != int):
            raise TypeError
        self.value*=other.value

    def __truediv__(self, other):
        if(other==0):
            raise ZeroDivisionError
        if (type(other) != int):
            raise TypeError
        self.value/=other

    def __repr__(self):
        return [self.zaehler,self.nenner]

"""Please NEVER EVER do something like this again QwQ"""