"""
v 1.4

Simpler version of hashlib that makes hashing easier.
Uses exact same algorithms as hashlib
So use a salted hash add 's' after the function.
Salt is a crypto random number of 64 bits
Can generate a random string using genrandstr(length)
Type info() for condensed help
"""
import secrets

#converts string to byte
def str2byte(str_variable):
    x = str(str_variable)
    x = x.encode()
    return x

#converts byte to string
def byte2str(byte_variable):
    x = byte_variable
    x = x.decode()
    return x

#sha512 hashing of a byte object
def sha512(x):
    import hashlib
    x = hashlib.sha512(x).hexdigest()
    x = str(x)
    x = x.encode()
    return byte2str(x)

#sha256 hashing of a byte object
def sha256(x):
    import hashlib
    x = hashlib.sha256(x).hexdigest()
    x = str(x)
    x = x.encode()
    return byte2str(x)

#md5 hashing of a byte object
def md5(x):
    import hashlib
    x = hashlib.md5(x).hexdigest()
    x = str(x)
    x = x.encode()
    return byte2str(x)

#sha1 hashing of a byte object
def sha1(x):
    import hashlib
    x = hashlib.sha1(x).hexdigest()
    x = str(x)
    x = x.encode()
    return byte2str(x)

#sha224 hashing of a byte object
def sha224(x):
    import hashlib
    x = hashlib.sha224(x).hexdigest()
    x = str(x)
    x = x.encode()
    return byte2str(x)

#sha384 hashing of a byte object
def sha384(x):
    import hashlib
    x = hashlib.sha384(x).hexdigest()
    x = str(x)
    x = x.encode()
    return byte2str(x)

#blake2b hashing of a byte object
def blake2b(x):
    import hashlib
    x = hashlib.blake2b(x).hexdigest()
    x = str(x)
    x = x.encode()
    return byte2str(x)

#blake2s hashing of a byte object
def blake2s(x):
    import hashlib
    x = hashlib.blake2s(x).hexdigest()
    x = str(x)
    x = x.encode()
    return byte2str(x)

#-----------------------------------------
#Salted hashes
#Just add an 's' after the name of the
#function you want salt with
#-----------------------------------------

#sha512 salted hashing of a byte object
def sha512s(x, salt=None):
    import hashlib
    if salt == None:
        salt = str(secrets.randbits(128))
    else:
        salt = str(salt)
    x = byte2str(x)
    x = x + salt
    x = str2byte(x)
    x = hashlib.sha512(x).hexdigest()
    x = str(x)
    x = x.encode()
    print('Salt:', salt)
    return byte2str(x)

#sha256 salted hashing of a byte object
def sha256s(x, salt=None):
    import hashlib
    if salt == None:
        salt = str(secrets.randbits(128))
    else:
        salt = str(salt)
    x = byte2str(x)
    x = x + salt
    x = str2byte(x)
    x = hashlib.sha256(x).hexdigest()
    x = str(x)
    x = x.encode()
    print('Salt:', salt)
    return byte2str(x)

#md5 salted hashing of a byte object
def md5s(x, salt=None):
    import hashlib
    if salt == None:
        salt = str(secrets.randbits(128))
    else:
        salt = str(salt)
    x = byte2str(x)
    x = x + salt
    x = str2byte(x)
    x = hashlib.md5(x).hexdigest()
    x = str(x)
    x = x.encode()
    print('Salt:', salt)
    return byte2str(x)

#sha1 salted hashing of a byte object
def sha1s(x, salt=None):
    import hashlib
    if salt == None:
        salt = str(secrets.randbits(128))
    else:
        salt = str(salt)
    x = byte2str(x)
    x = x + salt
    x = str2byte(x)
    x = hashlib.sha1(x).hexdigest()
    x = str(x)
    x = x.encode()
    print('Salt:', salt)
    return byte2str(x)

#sha224 salted hashing of a byte object
def sha224s(x, salt=None):
    import hashlib
    if salt == None:
        salt = str(secrets.randbits(128))
    else:
        salt = str(salt)
    x = byte2str(x)
    x = x + salt
    x = str2byte(x)
    x = hashlib.sha224(x).hexdigest()
    x = str(x)
    x = x.encode()
    print('Salt:', salt)
    return byte2str(x)

#sha384 salted hashing of a byte object
def sha384s(x, salt=None):
    import hashlib
    if salt == None:
        salt = str(secrets.randbits(128))
    else:
        salt = str(salt)
    x = byte2str(x)
    x = x + salt
    x = str2byte(x)
    x = hashlib.sha384(x).hexdigest()
    x = str(x)
    x = x.encode()
    print('Salt:', salt)
    return byte2str(x)

#blake2b salted hashing of a byte object
def blake2bs(x, salt=None):
    import hashlib
    if salt == None:
        salt = str(secrets.randbits(128))
    else:
        salt = str(salt)
    x = byte2str(x)
    x = x + salt
    x = str2byte(x)
    x = hashlib.blake2b(x).hexdigest()
    x = str(x)
    x = x.encode()
    print('Salt:', salt)
    return byte2str(x)

#blake2s salted hashing of a byte object
def blake2ss(x, salt=None):
    import hashlib
    if salt == None:
        salt = str(secrets.randbits(128))
    else:
        salt = str(salt)
    x = byte2str(x)
    x = x + salt
    x = str2byte(x)
    x = hashlib.blake2s(x).hexdigest()
    x = str(x)
    x = x.encode()
    print('Salt:', salt)
    return byte2str(x)

#Generates Cryptographically secure strings
def genrandstr(length):
    import random
    import string
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(int(length)))

def info():
    input('Version: 1.4\nCreated by Matthew Richards')
    print('-------------------------------------------------------------')
    input('Avaliable commands:\n')
    input("""str2byte(x)      Converts string to a byte
byte2str(x)      Converts byte to a string
md5(x)           Returns the md5 hash for a byte variable
sha512(x)        Returns the sha512 hash for a byte variable
sha256(x)        Returns the sha256 hash for a byte variable
sha1(x)          Returns the sha1 hash for a byte variable
sha224(x)        Returns the sha224 hash for a byte variable
sha384(x)        Returns the sha384 hash for a byte variable
blake2s(x)       Returns the blake2s hash for a byte variable
blake2b(x)       Returns the blake2b hash for a byte variable
To use salted hashes just add add 's' after the algorithm
To use a custom salt, add the salt after the byte variable
If no salt is given, then a custom salt is used.
Salts are crypto random 64 bit number
genrandstr(x)    Returns a random string of length x
info()           Displays the information about this module
changelog()      Displays the changelog for this library
""")
    
    input("""End Info
-------------------------------------------------------------\n""")
    print('File Path: Lib/hashes.py')

def Changelog():
    input("""Changelog:
v1.0: Added md5, sha1 - sha512
v1.1: Added blake2s and blake2b hash and info
v1.2: Added salted versions of hashes
v1.3: Added genrandstr
v1.4: Added changelog
v1.5: Added custom salts""")

__all__ = ['byte2str', 'str2byte', 'md5', 'md5s', 'sha512', 'sha512s', 'sha256'
           , 'sha256s', 'sha1', 'sha1s', 'sha224', 'sha224s', 'sha384', 'sha384s',
           'blake2s', 'blake2ss', 'blake2b', 'blake2bs', 'genrandstr', 'info',
           'Changelog']
