def prime_factors(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            print(i)
    if n > 1:
        print(n)

n = int(input('What to prime factorise? '))
print(prime_factors(n))
input('Press enter to end.')
