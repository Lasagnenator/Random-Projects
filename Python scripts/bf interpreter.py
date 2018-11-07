#BF interpreter
import sys
import os

ptr = [0]
pointer = 0
whilist = []
counter = 0

class PointerError(IndexError): pass
class CellError(ValueError): pass

def str2int(string):
    """Converts string to int list"""
    s = string
    #x = int(''.join(str(ord(c)) for c in s))
    x = [ord(c) for c in s]
    return x
    
def int2str(integer):
    """Converts int list to string""" 
    i = integer
    x = ''.join(chr(c) for c in i)
    return x

def runbf(arg, counter):
    if arg == '+':
         dp.increment()
    elif arg == '-':
         dp.decrement()
    elif arg == '>':
        dp.up()
    elif arg == '<':
        dp.down(counter)
    elif arg == '[': #set while pointer
        dp.setwhile()
    elif arg == ']': #goto while pointer, repeat until ptr = 0
        dp.endofwhile()
    elif arg == ',': #input
        dp.putchar()
    elif arg == '.': #output
        dp.valout()
    elif arg == '@':
        global ptr
        global pointer
        ptr = [0]
        pointer = 0

class dp():
    def up():
        global pointer
        global ptr
        pointer += 1
        #print('dp.up')
        try:
            temp = ptr[pointer]
        except IndexError:
            ptr.append(0)
    def down(pos):
        global pointer
        global ptr
        #print('dp.down')
        pointer -= 1
        if pointer < 0:
            raise PointerError('Data pointer has become negative at char {}'.format(pos+1))
    def increment():
        #print('dp.increment', end = '')
        global pointer
        global ptr
        ptr[pointer] += 1
        #print(ptr[pointer])
    def decrement():
        #print('dp.decrement', end = '')
        global pointer
        global ptr
        ptr[pointer] -= 1
        #print(ptr[pointer])
        if ptr[pointer] < 0:
            raise CellError('Data value has become negative at cell {}'.format(pointer))
    def putchar():
        #print('dp.putchar')
        global pointer
        global ptr
        s = str2int(input())
        i = 0
        for item in s:
            ptr[pointer+i] = item
            i += 1
    def valout():
        #print('dp.valout', end='')
        global pointer
        global ptr
        integer = ptr[pointer]
        #print(ptr[pointer])
        print(chr(integer), flush = True, end = '')
    def setwhile():
        #print('dp.setwhile')
        global counter
        global whilist
        #print('pointer = {}'.format(counter))
        whilist.append(counter)
    def endofwhile():
        #print('dp.endofwhile', end = '')
        global pointer
        global whilist
        global counter
        global ptr
        #log_list = []     
        if ptr[pointer] == 0:
            #log_list.append("!!!!!!! True\n")
            whilist.pop()
            #print('dp.endofwhile end-of-loop')
        else:
            #log_list.append("False\n")
            #print('dp.endofwhile continue-loop')
            counter = whilist[-1]
        #with open("C:/Users/Matthew/Desktop/Python/Python scripts/log.txt", "w") as file:
            #file.write(''.join(log_list5))
        

def main():
    try:
        global counter
        bfin = input('')
        bfcode = bfin
        while counter<len(bfcode):
            item = bfcode[counter]
            runbf(item, counter)
            counter = counter + 1
    except KeyboardInterrupt:
        print('KeyboardInterrupt')
        exitting = input('Exit? (Y/N)')
        if exitting.upper() == 'Y':
            exit()
    except:
        ertype, value, traceback = sys.exc_info()
        print('\nFailed: {}, {}'.format(str(ertype)[17:][:-2], value))

def noexceptions():
    global counter
    bfin = input('')
    bfcode = bfin
    while counter<len(bfcode):
        item = bfcode[counter]
        runbf(item, counter)
        counter = counter + 1

print('BF intepreter by Matthew Richards: Dynamic memory, Delete memory with @')
while True:
    #noexceptions()
    main()
    print('\nEnd of program.')
    ptr = [0]
    whilist = []
    counter = 0
    pointer = 0
