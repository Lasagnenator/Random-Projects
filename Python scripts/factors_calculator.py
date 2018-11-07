#note that this will take longer for bigger numbers

while True:
    num = int(input("Enter number to be tested:"))
    factors = []
    factornum = 0

    for i in range(1,num+1): #tests all numbers from 1 to the num
        if (num % i) == 0: #if the remainder of the number when it is divided by i is 0
            print(i) #prints i
            factors.append(i)
    factornum = len(factors)
    print("Finished") #says that the process is finished
    print('There are', factornum, 'factors in', num,':')
    print(str(factors))

input ("Press enter to close the program") #closes the program after pressing enter
