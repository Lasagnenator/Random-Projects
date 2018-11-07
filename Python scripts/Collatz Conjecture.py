#Collatz conjecture
def collatz(n):
    step = 0
    while True:
        step += 1
        if n == 0:
            return 0
        if n%2 == 0:
            n = n // 2
        elif n == 1:
            return step - 1
        else:
            n = n*3+1
        #if step % 10000 == 0:
            #print('.', end = '')

x = int(input('What number to start: '))
y1 = 0
while True:
    y = collatz(x)
    #if not (y1 == y):
        #print('\n{} takes {} steps to reach 1'.format(x, y), end = '\n')
        #y1 = y
    print('\n{} takes {} steps to reach 1'.format(x, y), end = '\n')
    x += 1
    

