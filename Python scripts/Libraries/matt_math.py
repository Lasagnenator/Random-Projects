#matt_math.py
"""Matthew Richards' implementation of the python math module"""

pi = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
halfpi = 1.57079632679489661923132169163975144209858469968755291048747229615390820314310449931401741267105853395
sqrtpi = 1.7724538509055159927515191031392484392904282050036823024429796190280631659214086355674772844431978746370902227969382486864740394743107959845636881148872452104072894051438123274274626807332635945385125
e = 2.718281828459045235360287471352662497757247093699959574966967627724076630353547594571382178525166427
tau = 6.2831853071795864769252867665590057683943387987502116419498891846156328125724179972560696506842341358
inf = 'Infinity'
neginf = '-Infinity'
nan = 'NaN'

from decimal import *
getcontext().prec = 100

def degrees(x):
    """convert x to degrees"""
    if x == 'Infinity' or x == '-Infinity':
        raise ValueError('Infinity cannot be represented as a float.')
    x /= 0.01745329251994329508887757483
    x %= 360
    return x
def radians(x):
    """converts x to radians"""
    if x == 'Infinity' or x == '-Infinity':
        raise ValueError('Infinity cannot be represented as a float.')
    x %= 360
    x *= 0.01745329251994329508887757483
    return x

def factorial(x):
    """factorial of x"""
    if x == 'Infinity' or x == '-Infinity':
        raise ValueError('Infinity cannot be represented as an integer.')
    if x == 0:
        return 1
    if x < 0:
        raise ValueError('Input was negative, use gamma function')
    if not float(x).is_integer():
        raise ValueError('Factorial function can only take positive integers. Use gamma function instead.')
    ans = 1
    for i in range(1, x+1):
        ans *= i
    return ans

def gcd(a, b):
    """finds gcd of a and b"""
    if a == 'Infinity' or a == '-Infinity':
        raise ValueError('Infinity cannot be represented as a float.')
    if b == 'Infinity' or b == '-Infinity':
        raise ValueError('Infinity cannot be represented as a float.')
    while b:
        a, b = b, a%b
    return a

def lcm(x, y):
    """lcm of a and b"""
    if x == 'Infinity' or x == '-Infinity':
        raise ValueError('Infinity cannot be represented as a float.')
    if y == 'Infinity' or y == '-Infinity':
        raise ValueError('Infinity cannot be represented as a float.')
    if x > y:
        greater = x
    else:
        greater = y

    while(True):
        if((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1

    return lcm

def sin(x):
    """finds sine of x in radians"""
    if x == 'Infinity' or x == '-Infinity':
        raise ValueError('Infinity cannot be represented as a float.')
    #x is in radians
    x = Decimal(radians(degrees(x)))
    p1 = Decimal(1/66319106593259530000)*Decimal(x**25)
    p2 = Decimal((-1)/663191065932595200)*Decimal(x**23)
    p3 = Decimal(1/7208598542745600)*Decimal(x**21)
    p4 = Decimal((-1)/85816649318400)*Decimal(x**19)
    p5 = Decimal(1/1129166438400)*Decimal(x**17)
    p6 = Decimal((-1)/16605388800)*Decimal(x**15)
    p7 = Decimal(1/276756480)*Decimal(x**13)
    p8 = Decimal((-1)/532240)*Decimal(x**11)
    p9 = Decimal(1/120960)*Decimal(x**9)
    p10 = Decimal((-1)/3360)*Decimal(x**7)
    p11 = Decimal(1/120)*Decimal(x**5)
    p12 = Decimal((-1)/6)*Decimal(x**3)
    ans = p1+p2+p3+p4+p5+p6+p7+p8+p9+p10+p11+p12+x
    return float(ans)

def cos(x):
    """finds cosine of x in radians"""
    if x == 'Infinity' or x == '-Infinity':
        raise ValueError('Infinity cannot be represented as a float.')
    #radians
    #cos(x)=sqrt(1-sin(x)**2)
#    ans = float(Decimal(1-sin(x)**2).sqrt())
    ans = float(Decimal(sin(x + halfpi)))
    return ans

def tan(x):
    """tangent of x in radians"""
    if x == 'Infinity' or x == '-Infinity':
        raise ValueError('Infinity cannot be represented as a float.')
    #radians
    #tan(x)= sin(x)/cos(x)
    cosX = cos(x)
    if cosX == 0:
        return inf
    return float(Decimal(sin(x))/Decimal(cosX))

def fabs(x):
    """find the abs of x"""
    if x == 'Infinity' or x == '-Infinity':
        raise ValueError('Infinity cannot be represented as a float.')
    ans = x.__abs__()
    return ans

def hypot(x, y):
    """sqrt(x*x+y*y)"""
    if x == 'Infinity' or x == '-Infinity':
        raise ValueError('Infinity cannot be represented as a float.')
    x = Decimal(x)
    y = Decimal(y)
    p1 = float(x*x+y*y)
    ans = sqrt(p1)
    return ans

def ceil(x):
    """Finds the highest int that is less than or equal to x"""
    if x == 'Infinity' or x == '-Infinity':
        raise ValueError('Infinity cannot be represented as a float.')
    strip = x%1
    x = float(x)
    if x.is_integer():
        return x
    elif x == 0:
        return 0
    elif strip >= 0.5 and x>0:
        x += 0.5
        ans = int(x)
    elif strip <=0.5 and x>0:
        ans = int(x)
    return ans

def floor(x):
    """Finds the lowest int greater than or equal to x"""
    if x == 'Infinity' or x == '-Infinity':
        raise ValueError('Infinity cannot be represented as a float.')
    x = float(x)
    if x.is_integer():
        return x
    elif x<0:
        ans = int(x-1)
    else:
        ans = int(x)
    return x

def pow(x, y):
    """equivalent to x**y"""
    if x == 'Infinity' or x == '-Infinity':
        raise ValueError('Infinity cannot be represented as a float.')
    if y == 'Infinity' or y == '-Infinity':
        raise ValueError('Infinity cannot be represented as a float.')
    ans = x**y
    return ans

def fsum(iterable):
    """Calculates a sum of floats with more precision"""
    ans = 0.0
    for item in iterable:
        if item == 'Infinity' or item == '-Infinity':
            raise ValueError('Infinity cannot be represented as a float.')
        ans = ans.__add__(item)
    return ans

def trunc(x):
    """truncates x to the nearest integer"""
    if x == 'Infinity' or x == '-Infinity':
        raise ValueError('Infinity cannot be truncated.')
    ans = 0
    if x<0:
        ans = int(x+1)
    elif x>0:
        ans = int(x)
    return ans

def modf(x):
    """returns the fractional and integer parts of x"""
    if x == 'Infinity' or x == '-Infinity':
        raise ValueError('Infinity cannot be represented as a float.')
    sign = x<0
    x = abs(x)
    integer = int(x)
    fract = x-integer
    if sign:
        integer *= -1
        fract *= -1
    return fract, integer

def isfinite(x):
    """Tests if x is a finite number"""
    integer = type(0)
    floating = type(0.0)
    try:
        temp = float(x)
        return True
    except ValueError:
        return False
    if x == inf:
        return False
    elif x == nan:
        return False
    if not ((type(x) == integer) or (type(x) == floating)):
        return False
    return True

def isinf(x):
    """Tests if x is Infinity of -Infinity"""
    if x == inf or x == neginf:
        return True
    else:
        return False

def isnan(x):
    """tests if x is NaN"""
    if x == nan:
        return True
    else:
        return False

def atan(x):
    """Computes the inverse tangent regardless of sign"""
    if x == 'Infinity' or x == '-Infinity':
        raise ValueError('Infinity cannot be represented as a float.')
    b = 0.52359877559829887307710723054658381403286156656251763682915743205130273438103483310467247089035284465
    k = 0.57735026918962576450914878050195745564760175127012687601860232648397767230293334569371539558574952520
    b0 = 0.261799387799149436538553615273291907016430783281258818414578716025651367190517416552336235445176422325
    k0 = 0.267949192431122706472553658494127633057194746189619371944193020548066983091199962918853813242751424317
    A = 0.999999020228907
    B = 0.257977658811405
    C = 0.59120450521312
    ang = 0
    x2 = 0
    comp = False
    hi_seg = False
    sign = x<0
    x = abs(x)
    if x>1:
        comp = True
        x = 1/x
    if x>k0:
        hi_seg = True
        x = (x-k)/(1+k*x)
    x2 = x*x
    ang = x*(A+B*x2)/(1+C*x2)
    if hi_seg:
        ang += b
    if comp:
        ang = halfpi - ang
    if sign:
        return radians(-ang)
    else:
        return radians(ang)
    
def atan2(y, x):
    """4-quadrant arctangent that takes into account the signs of y and x"""
    if x == 'Infinity' or x == '-Infinity':
        raise ValueError('Infinity cannot be represented as a float.')
    if y == 'Infinity' or y == '-Infinity':
        raise ValueError('Infinity cannot be represented as a float.')
    if x == 0:
        ans = halfpi
    else:
        ans = degrees(atan(abs(y/x)))
    if x<0:
        ans = pi-ans
    if y<0:
        ans = -ans
    return radians(ans)

def asin(x):
    """inverse sine"""
    if x == 'Infinity' or x == '-Infinity':
        raise ValueError('Infinity cannot be represented as a float.')
    if abs(x) >= 1:
        raise ValueError('Math domain error.')
    mid = x/(sqrt(1-x*x))
    ans = atan(mid)
    return ans

def acos(x):
    """inverse cosine"""
    if x == 'Infinity' or x == '-Infinity':
        raise ValueError('Infinity cannot be represented as a float.')
    if abs(x) >= 1:
        raise ValueError('Math domain error.')
    ans = 90-asin(x)
    return ans

def frexp(x):
    """Separates a float into mantissa and exponent"""
    if x == 'Infinity' or x == '-Infinity':
        raise ValueError('Infinity cannot be represented as a float.')
    def fexp(x):
        (sign, digits, exponent) = Decimal(x).as_tuple()
        return len(digits) + exponent - 1

    def fman(x):
        return float(Decimal(x).scaleb(-fexp(x)).normalize())

    exp = fexp(x)
    mant = fman(x)
    return mant, exp

def log1p(x):
    """Natural logarithm of x+1 in such a way that is more accurate when x is close to 0"""
    if x == 'Infinity' or x == '-Infinity':
        raise ValueError('Infinity cannot be represented as a float.')
    #base e log(x+1)
    div = 6720*x+840
    p1 = 855*(x*x*x*x*x*x*x)
    p2 = -(1000*(x*x*x*x*x*x))
    p3 = (1204*(x*x*x*x*x))
    p4 = -(1512*(x*x*x*x))
    p5 = 2030*(x*x*x)
    p6 = -(3080*(x*x))
    p7 = 6300*x
    p8 = 840
    ans = (x*(p1+p2+p3+p4+p5+p6+p7+p8))/div
    return ans

def log(x, base = e):
    """returns logarithm of x in variable base (default is e)"""
    def loge(x):
        #z = (x-1)/(x+1)
        #return (131072*z)/(480249)+(((16806499710*(z**9))-(184694590080*(z**7))+(622342641492*(z**5))-(816599349280*(z**3))+(365689776270*z))/(231*(-(7203735*(z**10))+(156080925*(z**8))-(936485550*(z**6))+(2274322050*(z**4))-(2400673275*(z**2))+(916620705))))
        m, p = frexp(float(x))
        p2 = 2.302585092994046*p
        nm = sqrt(m)
        y = (nm-1)/(nm+1)
        fract = 2*2*(y+(y*y*y)/3+(y**5)/5+(y**7)/7+(y**9)/9+(y**11)/11+(y**13)/13+(y**15)/15+(y**17)/17+(y**19)/19+(y**21)/21+(y**23)/23+(y**25)/25+(y**27)/27+(y**29)/29+(y**31)/31+(y**33)/33+(y**35)/35+(y**37)/37+(y**39)/39+(y**41)/41+(y**43)/43)
        return p2+fract
        #return float(format(p2+fract, '.1f'))
    if x < 0:
        raise ValueError('Math error, undefined value')
    if x == 0:
        return neginf
    if x == 'NaN':
        return 'NaN'
    if x == 'Infinity':
        return x
    if x == '-Infinity':
        return 'NaN'
    if base == e:
        return loge(x)
    p1 = loge(x)
    p2 = loge(base)
    ans = p1/p2
    return ans

def log10(x):
    """returns base 10 logarithm of x"""
    return log(x, 10)

def log2(x):
    """Returns a base 2 logarithm of x"""
    """
    n = len(bin(int(x))[2:])
    y = 2**(-n)*x
    m = 0
    z = 1
    def minilog(y, m, z):
        if y == 1:
            return 0
        elif y < 0.0000001:
            return 0
        else:
            while not (z>1 and z<5):
                m += 1
                z *= y
            return 2**(-m)+2**(-m)*minilog(z/2, 0, 1)
    minilog(y, m, z)
        
    if x == 1:
        return 0
    if not float(x).is_integer():
        raise ValueError('Input must be an int')
    binaryx = bin(x)[2:]
    intlog = len(binaryx)-1
    fraclog = int(binaryx[1:], 2)**2/(0.1242513487802389*x*x) #10 decimal precision
    return intlog+round(fraclog, 13)
    """
    return log(x, 2)

def sec(x):
    """secant"""
    if x == 'Infinity' or x == '-Infinity':
        raise ValueError('Infinity cannot be represented as a float.')
    if x%halfpi == 0:
        raise ValueError('Math error. Result Undefined')
    return 1/cos(x)

def cot(x):
    """cotangent"""
    if x == 'Infinity' or x == '-Infinity':
        raise ValueError('Infinity cannot be represented as a float.')
    if (x == 0) or (x%pi == 0):
        raise ValueError('Math error. Result Undefined')
    return 1/tan(x)

def csc(x):
    """cosecant"""
    if x == 'Infinity' or x == '-Infinity':
        raise ValueError('Infinity cannot be represented as a float.')
    if (x == 0) or (x%pi == 0):
        raise ValueError('Math error. Result Undefined')
    return 1/sin(x)

def cosh(x):
    """hyperbolic cosine"""
    if x == 'Infinity' or x == '-Infinity':
        raise ValueError('Infinity cannot be represented as a float.')
    return (exp(x)+exp(-x))/2

def sinh(x):
    """hyperbolic sine"""
    if x == 'Infinity' or x == '-Infinity':
        raise ValueError('Infinity cannot be represented as a float.')
    return (exp(x)-exp(-x))/2

def tanh(x):
    """hyperbolic tangent"""
    if x == 'Infinity' or x == '-Infinity':
        raise ValueError('Infinity cannot be represented as a float.')
    if x > 19:
        return 1.0
    return (exp(x)-exp(-x))/(exp(x)+exp(-x))

def csch(x):
    """hyperbolic cosecant"""
    if x == 'Infinity' or x == '-Infinity':
        raise ValueError('Infinity cannot be represented as a float.')
    return 2/(exp(x)-exp(-x))

def sech(x):
    """hyperbolic secant"""
    if x == 'Infinity' or x == '-Infinity':
        raise ValueError('Infinity cannot be represented as a float.')
    return 2/(exp(x)+exp(-x))

def coth(x):
    """hyperbolic cotangent"""
    if x == 'Infinity' or x == '-Infinity':
        raise ValueError('Infinity cannot be represented as a float.')
    return (exp(2*x)+1)/(exp(2*x)-1)

def copysign(x, y):
    """replaces the sign of x with the sign of y and returns x"""
    if x == 'Infinity' or x == '-Infinity':
        raise ValueError('Infinity cannot be represented as a float.')
    if y == 'Infinity' or y == '-Infinity':
        raise ValueError('Infinity cannot be represented as a float.')
    if y < 0:
        return -abs(x)
    elif y > 0:
        return abs(x)

def fmod(x, y):
    """Mathematical definition of modulo for x%y"""
    if x == 'Infinity' or x == '-Infinity':
        raise ValueError('Infinity cannot be represented as a float.')
    if y == 'Infinity' or y == '-Infinity':
        raise ValueError('Infinity cannot be represented as a float.')
    if float(log(x, 2)).is_integer() and x>0:
        return x&(2**y-1)
    x = Decimal(x)
    y = Decimal(y)
    return float(x-(y*int(x/y)))

def atanh(x):
    """inverse hyperbolic tangent"""
    if x == 'Infinity' or x == '-Infinity':
        raise ValueError('Infinity cannot be represented as a float.')
    if abs(x) > 1:
        raise ValueError('Math error. Result Undefined')
    return 0.5*(log((1+x)-log(1-x)))

def asinh(x):
    """invere hyperbolic sine"""
    if x == 'Infinity' or x == '-Infinity':
        raise ValueError('Infinity cannot be represented as a float.')
    return log(x+sqrt(1+x*x))

def acosh(x):
    """inverse hyperbolic cosine"""
    if x == 'Infinity' or x == '-Infinity':
        raise ValueError('Infinity cannot be represented as a float.')
    if x <1:
        raise ValueError('Math error. Result Undefined')
    if x == 1:
        return 0
    return log(x+sqrt(x-1)*sqrt(x+1))

def acsch(x):
    """inverse hyperbolic cosecnt"""
    if x == 'Infinity' or x == '-Infinity':
        raise ValueError('Infinity cannot be represented as a float.')
    if x == 0:
        raise ValueError('Math error. Result Undefined')
    return log(sqrt(1+(1/(x*x)))+(1/x))

def acoth(x):
    """inverse hyperbolic cotangent"""
    if x == 'Infinity' or x == '-Infinity':
        raise ValueError('Infinity cannot be represented as a float.')
    if abs(x) < 1:
        raise ValueError('Math error. Result Undefined')
    if abs(x) == 1:
        raise ValueError('Math error. Result Undefined')
    return 0.5*(log(1+1/x)-log(1-1/x))

def asech(x):
    """inverse hyperbolic secant"""
    if x == 'Infinity' or x == '-Infinity':
        raise ValueError('Infinity cannot be represented as a float.')
    if x > 1:
        raise ValueError('Math error. Result Undefined')
    if x == 1:
        return 0
    return log(sqrt(1/x-1)*sqrt(1/x+1)+1/x)

def ldexp(x, i):
    """equvalent to x*(2^i)"""
    if x == 'Infinity' or x == '-Infinity':
        raise ValueError('Infinity cannot be represented as a float.')
    return x*(2**i)

def series(start, stop, function):
    """Calculates a sum between start and stop by using function to create a definite value.
Function must be a valid function"""
    if stop == '-Infinity' or stop == 'Infinity':
        raise ValueError('Infinity cannot be a stopping point.')
    if start == '-Infinity' or start == 'Infinity':
        raise ValueError('Infinity cannot be a starting point')
    ans = 0
    for k in range(start, stop+1):
        ans += function(k)
    return ans

def summation(start, stop, function, x):
    """Calculates a sum between start and stop by using function to create a variable value.
Function must be a valid function as function(k, x)"""
    if stop == '-Infinity' or stop == 'Infinity':
        raise ValueError('Infinity cannot be a stopping point.')
    if start == '-Infinity' or start == 'Infinity':
        raise ValueError('Infinity cannot be a starting point')
    ans = 0
    for k in range(start, stop+1):
        ans += function(k, x)
    return ans

def product(start, stop, function, x):
    """Calculates a product between start and stop by using function to create a variable value.
Function must be a valid function as function(k, x)"""
    if stop == 'Infinity':
        raise ValueError('Infinity cannot be a stopping point.')
    if start == '-Infinity' or start == 'Infinity':
        raise ValueError('Infinity cannot be a starting point')
    ans = 1
    for k in range(start, stop+1):
        ans *= function(k, x)
    return ans

def erf(x):
    """Calculates the error function at x"""
    if x == 'Infinity' or x == '-Infinity':
        raise ValueError('Infinity cannot be represented as a float.')
    if x > 5.92:
        return 1
    if x < -5.92:
        return 1
    def function(n, z):
        ans = ((-1)**n*z**(2*n+1))/(factorial(n)*(2*n+1))
        return ans
    p1 = 2/sqrtpi
    ans = 0
    for i in range(18):
        ans += function(i, x)
    ans *= p1
    return ans

def erfc(x):
    """Calculates the complementary error function at x."""
    if x == 'Infinity' or x == '-Infinity':
        raise ValueError('Infinity cannot be represented as a float.')
    return 1-erf(x)

def expm1(x):
    """Calculates e**x-1 with better precision than doing e**x-1 when x is small."""
    if x == 'Infinity' or x == '-Infinity':
        raise ValueError('Infinity cannot be represented as a float.')
    if x>1:
        return exp(x)-1
    ans = 0
    for i in range(1, 12):
        ans += (x**i)/factorial(i)
    return ans

def isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0):
    """Calculates if a number is close to another number within a certain range."""
    if a==nan or b==nan:
        return False
    elif a==inf and b == inf:
        return True
    elif a==neginf and b==neginf:
        return True
    aa = abs(a)
    ab = abs(b)
    if abs(max(a,b)-min(a,b)) <= rel_tol: #relatiive closeness
        return True
    if abs(max(aa, ab)-min(aa, ab)) <= abs_tol: #absolute closeness
        return True
    return False

def npr(n, r):
    """Calculates the permutations of r in n"""
    if r == 'Infinity' or r == '-Infinity':
        raise ValueError('Infinity cannot be represented as a float.')
    if n == 'Infinity' or n == '-Infinity':
        raise ValueError('Infinity cannot be represented as a float.')
    integer = type(0)
    if type(n) != integer or type(r) != integer:
        raise ValueError('Reult Undefined for fractional values')
    if n < 0 or r<0:
        raise ValueError('Math error. Result undefined for negative values')
    return int(factorial(n))/(factorial(n-r))

def ncr(n, r):
    """Calculates the combinations of r in n"""
    if r == 'Infinity' or r == '-Infinity':
        raise ValueError('Infinity cannot be represented as a float.')
    if n == 'Infinity' or n == '-Infinity':
        raise ValueError('Infinity cannot be represented as a float.')
    integer = type(0)
    if type(n) != integer or type(r) != integer:
        raise ValueError('Reult Undefined for fractional values')
    if n < 0 or r<0:
        raise ValueError('Math error. Result undefined for negative values')
    return int(npr(n, r)/factorial(r))

def lgamma(x):
    """Calculates the natural logarithm of the abs(gamma(x))"""
    if x == 'Infinity' or x == '-Infinity':
        raise ValueError('Infinity cannot be represented as a float.')
    if x>0 and float(x).is_integer():
        x = int(x)
        return series(1, x, log)
    return log(abs(gamma(x)))

def root(x, r):
    """Calculates rth root of x to 13 significant figures"""
    if x == 'Infinity' or x == '-Infinity':
        raise ValueError('Infinity cannot be represented as a float.')
    if r == 'Infinity' or r == '-Infinity':
        raise ValueError('Infinity cannot be represented as a float.')
    if r == 2:
        return sqrt(x)
    if r == 1:
        return x
    if x == 1:
        return 1.0
    low = 0
    high = x
    mid = 0
    min_range = 0.00000000000001
    
    while high-low > min_range:
        mid = (low + high) / 2.0
        test = 1
        test = mid**r
        if abs(test - x) <= min_range:
            return mid
        elif test < x:
            low = mid
        else:
            high = mid
    return round(mid, 13)

def sqrt(x):
    """Finds the sqrt of x"""
    if x == 'Infinity' or x == '-Infinity':
        raise ValueError('Infinity cannot be represented as a float.')
    #binary search approximation
    if x == 1:
        return 1.0
    low = 0
    high = x
    mid = 0
    min_range = 0.00000000000001
     
    while high - low > min_range:
        mid = (low + high) / 2.0
        test = mid * mid
        if low==high:
            return low
        if abs(test - x) <= min_range:
            return mid
        elif test < x:
            low = mid
        else:
            high = mid
    return mid

def sinc(x):
    """sinc function of x"""
    if x == 0:
        return 1
    return sin(x)/x

def sinhc(x):
    """hyperbolic sinc function of x"""
    if x == 0:
        return 1
    return sinh(x)/x

def tanc(x):
    """tanc function of x"""
    if x == 0:
        return 1
    return tan(x)/x

def tanhc(x):
    if x == 0:
        return 1
    return tanh(x)/x

def hacovercosine(x):
    """Hacovercosine of x"""
    return 0.5*(1+sin(x))

def hacoversine(x):
    """Hacoversine of x"""
    return 0.5*(1-sin(x))

def coversine(x):
    """Coversine of x"""
    return 1-sin(x)

def covercosine(x):
    """Covercosine of x"""
    return 1+sin(x)

def versine(x):
    """Versine of x"""
    return 1-cos(x)

def vercosine(x):
    """Vercosine of x"""
    return 1+cos(x)

def excosecant(x):
    return csc(x)-1

def exsecant(x):
    return sec(x)-1

def haversine(x):
    return sin(0.5*x)**2

def havercosine(x):
    return 0.5*(1+cos(x))

def hypot3(x, y ,z):
    """equivalent to sqrt(x*x+y*y+z*z)"""
    return sqrt(x*x+y*y+z*z)

def rtriangle(s1, s2, h):
    p1 = hypot(s1, s2)
    return isclose(p1, h)

def integral(formula, high, low):
    """Formula is like:
y = <formula using x (must be string)>"""
    from numpy import arange
    n=99999
    steps = n*(abs(high)+abs(low))
    step_size = (high-low)/steps
    assert step_size > 0
    x = arange(low, high, step_size)
    y = eval(formula)
    y *= step_size
    y = y.tolist()
    ans = sum(y)
    return round(ans, 4)

#----------------------------
#WORK IN PROGRESS FUNCTIONS

def gamma(x):
    """Calculates the gamma function of a number to 9 dp.
gamma(x) == factorial(n-1)"""
    if x == 'Infinity' or x == '-Infinity':
        raise ValueError('Infinity cannot be represented as a float.')
    #if x>0 and float(x).is_integer():
        #return float(factorial(x-1))
    if x<0 and float(x).is_integer():
        raise ValueError('Math error. Result undefined for negative integer values')
    if x==0:
        return 1.0
    #Integral solving; does not work with negatives.
    if x > 0:
        return integral('x**({}-1)*e**(-x)'.format(x), 50, 0)
    
    #adapted from wikipedia's lanczo approximation
    #https://en.wikipedia.org/wiki/Lanczos_approximation#Simple_implementation
    z = float(x)
    if z<0:
        return (-pi)/(-z*gamma(-z)*sin(pi*z))
    q = [75122.6331530, 80916.6278952, 36308.2951477, 8687.24529705,
         1168.92649479, 83.8676043424, 2.50662827511]
    N = 7
    p1 = 0
    p2 = 1
    for n in range(0, N):
        p1 += q[n]*(z**n)
    for n in range(0, N):
        p2 *= (z+n)
    p3 = (z+5.5)**(z+0.5)*exp(-(z+5.5))
    return (p1/p2)*p3

def exp(x):
    """Calculates e**x with more precision for x close to 0"""
    if x == 'Infinity' or x == '-Infinity':
        raise ValueError('Infinity cannot be represented as a float.')
    return e**x
    if abs(x) > 1:
        return e**x
    n = round(x)
    r = x-n
    integer = e**n
    frac = 1+(r*r)/2+(r*r*r)/6+(r**4)/24+(r**5)/120+(r**6)/720+(r**7)/5040+(r**8)/40320+(r**9)/362880+(r**10)/3628800
    return round(float(integer*Decimal(str(frac))), 15)
       
#----------------------------
#END OF IN PROGRESS FUNCTIONS

__all__ = {'integral', 'hypot3', 'tanhc', 'havercosine', 'haversine', 'exsecant', 'excosecant', 'vercosine', 'versine', 'coversine', 'covercosine', 'hacoversine', 'hacovercosine', 'product', 'summation', 'acos', 'acosh', 'acoth', 'acsch', 'asech', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'csc', 'csch', 'cot', 'coth', 'degrees', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'ncr', 'npr', 'pow', 'radians', 'root', 'sec', 'sech', 'sin', 'sinc', 'sinh', 'sqrt', 'summation', 'tan', 'tanh', 'tanc', 'trunc'}
__version__ = '1.4'
__credits__ = """Matthew Richards - 90%
Mathworld.wolframalpha.com - 10%"""
__WIP_FUNCTIONS__ = {'gamma', 'exp'}
__CUSTOM_FUNCTIONS__ = {'integral', 'hypot3', 'tanhc', 'havercosine', 'haversine', 'exsecant', 'excosecant', 'vercosine', 'versine', 'coversine', 'covercosine', 'hacovercosine', 'hacoversine', 'summation', 'product', 'csc', 'csch', 'acsch', 'cot', 'coth', 'acoth', 'ncr', 'npr', 'root', 'sec', 'sech', 'asech', 'sinc', 'sinhc', 'series', 'tanc'}
