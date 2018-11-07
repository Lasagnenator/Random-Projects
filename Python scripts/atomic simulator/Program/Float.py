#custom floatingpoint numbers
from decimal import *
import math

div_prec = 20

class UnsupportedError(): pass

class Float():
    """Floating point numbers that do not lose precision in large/small
numbers with many decimal places
The 'Object' is called
Internally stored as (exponent, mantissa, sign)"""

    #floats are stored as: sign*a*(10**b)
    exponent = 0 #integer -infinity~infinity
    mantissa = 0 #integer 0~infinity
    sign = 1     #-1 or 1
    def __init__(self, obj=None):
        if type(obj) == type(()) and len(obj)==3:
            if not float(obj[1]).is_integer():
                rmant = 0.1
                adjust = 1
                while not rmant.is_integer():
                    adjust *= 10
                    rmant = (obj[1] * adjust)
                    rexp = (obj[0] - (math.log10(adjust)))
            elif obj[1]%10 != 0:
                rexp = (obj[0])
                rmant = (obj[1])
            elif obj[1] != 0:
                #print(obj)
                adjust = int(math.log10(obj[1]))
                rmant = obj[1]/(10**adjust)
                rexp = obj[0]+adjust
                if not float(rmant).is_integer():
                    smant = 0.1
                    adjust = 1
                    while not smant.is_integer():
                        adjust *= 10
                        smant = (rmant * adjust)
                        sexp = (rexp - (math.log10(adjust)))
                    rmant = smant
                    rexp = sexp
            else:
                rexp = 0
                rmant = 0
            self.exponent = int(rexp)
            self.mantissa = int(rmant)
            self.sign = obj[2]
            if not(abs(self.sign)==1):
                raise ValueError('Sign must be -1 or 1. Sign was {}'.format(obj[2]))
        elif type(obj) == Float:
            self.exponent = obj.exponent
            self.mantissa = obj.mantissa
            self.sign = obj.sign
            self = obj
        elif obj != None:
            def fexp(x):
                (sign, digits, exponent) = Decimal(x).as_tuple()
                return len(digits) + exponent - 1

            def fman(x):
                return float(Decimal(x).scaleb(-(len(Decimal(x).as_tuple()[1])+Decimal(x).as_tuple()[2]-1)).normalize())
            def fsign(x):
                if x<0:
                    return -1
                elif x >= 0:
                    return 1
            exp = fexp(obj)
            mant = fman(obj)
            #print((exp, mant))
            rmant = 0.1
            adjust = 1
            if not float(mant).is_integer():
                if not rmant.is_integer():
                    while not rmant.is_integer():
                        adjust *= 10
                        rmant = mant * adjust
                        rexp = exp - int(math.log10(adjust))
                        #print(rexp)
                else:
                    rmant = mant
                    rexp = exp
            else:
                rexp = exp
                rmant = int(mant)
            if (rmant/10).is_integer():
                while (rmant/10).is_integer():
                    rmant /= 10
                    rexp += 1
            #print(adjust)
            self.sign = fsign(float(obj))
            self.exponent = rexp
            self.mantissa = int(abs(rmant))
        if self.mantissa == 0:
            self.exponent = 0
            self.sign = 1
            self.mantissa = 0
    def __abs__(self):
        return Float((self.exponent, self.mantissa, 1))
    def __add__(self, value):
        """Return self+value"""
        value = Float(value)
        adjust = (max(self.exponent, value.exponent)-min(self.exponent, value.exponent))
        if self>value:
            self.exponent += adjust
            self.mantissa *= int(10**adjust)
        else:
            value.exponent += adjust
            value.mantissa *= int(10**adjust)
        self.mantissa *= self.sign
        value.mantissa *= value.sign
        rmant = self.mantissa + value.mantissa
        #print(rmant)
        if rmant < 0:
            sign = -1
        else:
            sign = 1
        rmant = abs(rmant)
        return Float((self.exponent, rmant, sign))
    def __sub__(self, value):
        return Float(self)+(-Float(value))
    def __bool__(self):
        if self.mantissa == 0:
            return False
        else:
            return True
    def __call__(self):
        print("""This is a floating-point library that aims to not lose precision with any number of calculations.""")
        return self
    def __contains__(self, key):
        if key=='exponent' or key=='mantissa' or key=='sign':
            return True
        else:
            return False
    def __eq__(self, value):
        """Return self==value"""
        value = Float(value)
        if self.exponent == value.exponent and self.mantissa == value.mantissa and self.sign == value.sign:
            return True
        else:
            return False
    def __float__(self):
        """Return float(self)"""
        #return float(str(self))
        return float(self.mantissa*(10**self.exponent)*self.sign)
    def __getitem__(self, pos):
        """Return self[key]
Can be 0,1,2,exponent,mantissa,sign"""
        if pos == 0:
            return self.exponent
        elif pos == 1:
            return self.mantissa
        elif pos == 2:
            return self.sign
        elif pos.lower() == 'exponent':
            return self.exponent
        elif pos.lower() == 'mantissa':
            return self.mantissa
        elif pos.lower() == 'sign':
            return self.sign
        else:
            raise IndexError('Key out of range')
    def __setitem__(self, key, value):
        if type(key) == str:
            self.key = value
        elif type(key) == int:
            if key == 0:
                self.exponent = value
            elif key == 1:
                self.mantissa = value
            elif kye == 2:
                self.sign == value%1
    def __ge__(self, value):
        """Return self>=value"""
        if self>value or self == value:
            return True
        else:
            return False
    def __gt__(self, value):
        """Return self>value"""
        value = Float(value)
        if self.exponent>value.exponent:
            return True
        elif self.sign*self.mantissa>value.sign*value.mantissa and self.exponent == value.exponent:
            return True
        else:
            return False
        pass
    def __int__(self):
        if self.exponent < -1:
            return 0
        return int(float(self))
    def __le__(self, value):
        """Return self<=value"""
        if self<value or self == value:
            return True
        elif self.sign*self.mantissa<value.sign*value.mantissa and self.exponent == value.exponent:
            return True
        else:
            return False
    def __len__(self):
        return 3
    def __lt__(self, value):
        """Return self<value"""
        value = Float(value)
        if self.exponent<value.exponent:
            return True
        elif self.sign*self.mantissa>value.sign*value.mantissa and self.exponent == value.exponent:
            return True
        else:
            return False
    def __mul__(self, value):
        """Return self*value"""
        value = Float(value)
        rexponent = self.exponent+value.exponent
        rmantissa = self.mantissa*value.mantissa
        sign = self.sign*value.sign
        ans = Float((rexponent, rmantissa, sign))
        return ans
    def __truediv__(self, value):
        """Return self/value
---> Does not round off the last decimal point!
Precision can be changed through div_prec (usually Float.div_prec)

>>> import Float
>>> Float.div_prec = x

div_prec must always be a positive integer!"""
        value = Float(value)
        self.mantissa *= 10**div_prec
        self.exponent -= div_prec
        rmant = self.mantissa//value.mantissa
        rexp = self.exponent - value.exponent
        sign = self.sign*value.sign
        #print((rexp, rmant, sign))
        return Float((rexp, rmant, sign))
    def __mod__(self, value):
        """Return self%value"""
        value = Float(value)
        return self-(value*(self/value))
        pass
    def __ne__(self, value):
        """Return self!=value"""
        if self == value:
            return False
        else:
            return True
    def __neg__(self):
        """Return -self"""
        return Float((self.exponent, self.mantissa, self.sign*-1))
    def __pos__(self):
        return Float(self.exponent, self.mantissa, 1)
    def __pow__(self, value):
        """Returns self**value
WIP!"""
        value = Float(value)
        def exp(x):
            z = x
            return 1/(
                1-(z/(
                    1+(z/(
                        2-(z/(
                            3+(z/(
                                2-(z/(
                                    5+(z/(
                                        2-(z/(
                                            7+(z/(
                                                2-(z/(
                                                    9+(z/(
                                                        2-(z/(
                                                            11+(z/(
                                                                2-(z/(
                                                                    13+(z/(
                                                                        2-(z/(
                                                                            15+(z/2))))))))))))))))))))))))))))))))
        def log(x):
            x -= 1
            #if x<=0:
                #raise ValueError('Logarithm undefined for values: x <= 0')
            return x/(
                1+(x/(
                    2+(x/(
                        3+((4*x)/(
                            4+((4*x)/(
                                5+((9*x)/(
                                    6+((9*x)/(
                                        7+((16*x)/(
                                            8+((16*x)/(
                                                9+((25*x)/(
                                                    10+((25*x)/(
                                                        11+((36*x)/(
                                                            12+((36*x)/(
                                                                13+((49*x)/(
                                                                    14+((49*x)/(
                                                                        15+((64*x)/(
                                                                            16+((64*x)/(
                                                                                17+((81*x)/(
                                                                                    18+((81*x)/(
                                                                                        19+((100*x)/(
                                                                                            20)))))))))))))))))))))))))))))))))))))))
        "self**value"
        return exp(value*log(self))
    def __repr__(self):
        return 'Float(({!r}, {!r}, {!r}))'.format(self.exponent, self.mantissa, self.sign)
    def __radd__(self, value):
        """Return value+self"""
        return self+value
    def __rsub__(self, value):
        """Return value-self"""
        return -self+value
    def __rmul__(self, value):
        """Return value*self"""
        return self*value
    def __round__(self, n=0):
        """If n == 0 then round to neraest integer
else, round to n digits"""
        if n == 0:
            return int(self)
        elif n<0:
            raise ValueError('n digits cannot be less than 0! n was {}'.format(n))
        rmant = int(str(self.mantissa)[:(n+1)])
        if self.exponent < 0:
            rexp = -n
        else:
            rexp = self.exponent
        return Float((rexp, rmant, self.sign))
    def __rtruediv__(self, value):
        """Return value/self"""
        value = Float(value)
        return value/self
    def __rmod__(self, value):
        """Return value%self"""
        value = Float(value)
        return value%self
    def rpow(self, value):
        """Returns value**self
WIP!"""
        value = Float(value)
        return value**self
    def __rshift__(self, value):
        """Returns self>>value"""
        return Float((self.exponent-value, self.mantissa, self.sign))
    def __lshift__(self, value):
        """Returns self<<value"""
        return Float((self.exponent+value, self.mantissa, self.sign))
    def __str__(self):
        if self.exponent>0:
            return str(self.mantissa)+('0'*self.exponent)
        elif self.exponent == 0:
            return str(self.mantissa)
        return '{}e({})'.format(self.mantissa*self.sign, self.exponent)
    def __hash__(self):
        from hashlib import sha512
        return int(sha512(str(self.exponent+self.mantissa+self.sign).encode()).hexdigest(), 16)
    def as_tuple(self):
        """Returns (exponent, mantissa, sign)"""
        return self.exponent, self.mantissa, self.sign
    
