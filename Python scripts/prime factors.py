#find prime factors

import math as m
from multiprocessing.dummy import Pool as ThreadPool

pool = ThreadPool(4)

def genprimes(limit): # derived from 
                      # Code by David Eppstein, UC Irvine, 28 Feb 2002
    D = {}            # http://code.activestate.com/recipes/117119/
    q = 2
    count = 0

    #while q <= limit:
    while count < limit:
        if q not in D:
            yield q
            D[q * q] = [q]
            count += 1
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1

high = int(input("Number: "))
prime_end_high = int((high))
prime_list = pool.map(lambda x: x, genprimes(high))
pool.close()
pool.join()
#prime_list = [i for i in genprimes(prime_end_high)]
p_factors = []
input("Stopper before finding prime factors.")

try:
    pass
except Exception as e:
    print(e)
except KeyboardInterrupt:
    pass
finally:
    for prime in prime_list:
        if prime>high:
           pass
        elif high%prime==0:
           p_factors.append(prime)
    input('Exiting')

