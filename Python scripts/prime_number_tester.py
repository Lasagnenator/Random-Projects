import math as m
import sys

try:
    while True:
        high = int(input("Enter max number to be tested."))

        num = 2
        prime_list = [2]

        for num in range(3, high + 1, 2):
            for i in prime_list:
                if i>m.sqrt(num):
                    pass
                elif (num % i) == 0: #Not prime
                    break
            else: #Prime
                prime_list.append(num)
        print(prime_list)
        approx = int(high/(m.log(high)-1))
        print('Approximate number of primes: {}'.format(approx))
        print('Length:', len(prime_list))
except Exception as e:
    print(e)
except KeyboardInterrupt:
    pass
finally:
    input('Exiting')
    sys.exit()

