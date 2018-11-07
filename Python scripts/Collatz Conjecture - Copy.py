#Collatz conjecture
def collatz(n):
    step = 0
    while True:
        step += 1
        print(n, end = '\n')
        if n == 0:
            return 0
        if n%2 == 0:
            n = n // 2
            #print('2', end = '')
        elif n == 1:
            print('\n')
            return step - 1
        else:
            n = n*3+1
            #print('1', end = '')
        #if step % 10000 == 0:
            #print('.', end = '')


    

