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

#x = int(input('What number to start: '))
#file = input('Directory to the txt file to output to.')
f = open('C:/Users/Matthew/Desktop/Python/Python scripts/Collatz table.txt', 'a')
#f.write('(')
try:
    x = int(input('What number to start: '))
    while True:
        y = collatz(x)
        str2write = '{}, {}\n'.format(x, y)
        f.write(str2write)
        f.flush()
        x += 1
except:
    #f.write(')')
    pass

f.close()
print('File saved.')
input('Press enter to end')

