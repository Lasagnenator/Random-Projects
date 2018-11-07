#Hash cracker
import hashes as h
import string

valid_strs = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
#letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

#global valid_strs

def md5(string):
    try:
        string = string.encode()
    except AttributeError:
        pass
    return h.md5(string)

def sha512(string):
    try:
        string = string.encode()
    except AttributeError:
        pass
    return h.sha512(string)

def sha256(string):
    try:
        string = string.encode()
    except AttributeError:
        pass
    return h.sha256(string)

def testmd5(hashed, chars):
    for a in chars:
        if md5(a)==hashed:
            return a
        for b in chars:
            if md5(a+b)==hashed:
                return a+b
            for c in chars:
                if md5(a+b+c)==hashed:
                    return a+b+c
                for d in chars:
                    if md5(a+b+c+d)==hashed:
                        return a+b+c+d
                    for e in chars:
                        if md5(a+b+c+d+e)==hashed:
                            return a+b+c+d+e

def testsha512(hashed, chars):
    for a in chars:
        if sha512(a)==hashed:
            return a
        for b in chars:
            if sha512(a+b)==hashed:
                return a+b
            for c in chars:
                if sha512(a+b+c)==hashed:
                    return a+b+c
                for d in chars:
                    if sha512(a+b+c+d)==hashed:
                        return a+b+c+d
                    for e in chars:
                        if sha512(a+b+c+d+e)==hashed:
                            return a+b+c+d+e

def testsha256(hashed, chars):
    for a in chars:
        if sha256(a)==hashed:
            return a
        for b in chars:
            if sha256(a+b)==hashed:
                return a+b
            for c in chars:
                if sha256(a+b+c)==hashed:
                    return a+b+c
                for d in chars:
                    if sha256(a+b+c+d)==hashed:
                        return a+b+c+d
                    for e in chars:
                        if sha256(a+b+c+d+e)==hashed:
                            return a+b+c+d+e

while True:
    hashed = (input('Hash to crack: '))
    choice_of_strings = input('letters, numbers, letternum, allchars: ')
    alg = input("""What algorithm:
    Valid:
    sha512
    md5
    sha256
    """)

    if choice_of_strings == 'letters':
        chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    elif choice_of_strings == 'numbers':
        chars = '0123456789'
    elif choice_of_strings == 'letternum':
        chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ012346789'
    elif choice_of_strings == 'allchars':
        chars = valid_strs

    unhashed = 'UNABLE_TO_DE-HASH'

    if alg == 'sha512':
        unhashed = testsha512(hashed, chars)
    elif alg == 'sha256':
        unhashed = testsha256(hashed, chars)
    elif alg == 'md5':
        unhashed = testmd5(hashed, chars)

    if unhashed == 'UNABLE_TO_DE-HASH':
        print('No hash found')
    else:
        print('string = {}'.format(unhashed))



