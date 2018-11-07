#graphs the Collatz table
from matplotlib import pyplot

print('Generating graph.')

try:
    with open('C:/Users/Matthew/Desktop/Python/Python scripts/Collatz table.txt', 'r') as ins:
        for line in ins:
            numvalue = str(line).strip('\n')
            x, y = [int(x) for x in numvalue.split(',')]
            pyplot.scatter(x, y, c = 'r', marker = '.')
        pyplot.show()
except KeyboardInterrupt:
    print('Alright then, I\'ll generate the graph for you')
    pyplot.show()

input('Press enter to end.')
