#strings = '0123456789abcdefghijklmnopqrstuvwxyz'
strings = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#strings = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
f = open('list.txt', 'a')
for a in strings:
    f.write('Wireless@'+a+'\n')
print('1-character finished')
f.flush()
for a in strings:
    for b in strings:
        f.write('Wireless@'+a+b+'\n')
print('2-character finished')
f.flush()
for a in strings:
    for b in strings:
        for c in strings:
            f.write('Wireless@'+a+b+c+'\n')
print('3-character finished')
f.flush()
for a in strings:
    for b in strings:
        for c in strings:
            for d in strings:
                f.write('Wireless@'+a+b+c+d+'\n')
print('4-character finished')
f.flush()
input('Paused.')
for a in strings:
    for b in strings:
        for c in strings:
            for d in strings:
                for e in strings:
                    f.write('Wireless@'+a+b+c+d+e+'\n')
print('5-character finished')
f.flush()
input('Finished')
