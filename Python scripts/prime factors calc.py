#finds prime factors WIP
num = int(input('Enter the number to be factorised: '))

for i in range(1,num + 1):
    if (num % i) == 0: #Check if i is factor
        for q in range(1, i): #Check if i is prime
            if i%q == 0:
                break
            else:
                print(i)
    pass

print('Finished')
input('Press end to end the program')
