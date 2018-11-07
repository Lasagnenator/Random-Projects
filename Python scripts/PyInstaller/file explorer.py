#File explorer
import os
import sys
from tkinter import Tk
from tkinter.filedialog import asksaveasfilename

Tk().withdraw()
curpath = sys.path[1]

while curpath != os.path.dirname(curpath):
    curpath = os.path.dirname(curpath)
print('Root directory: {} \n'.format(curpath))
if bool(input('Set custom root directory? (press any key then enter for True)')):
    curpath = input('Custom root directory: ')
    print('\n'+'New Root: {}'.format(curpath))
print()
root = curpath
files = ''

try:

    while True:
        for item in os.listdir(curpath):
            files += item + '\n'
        files += '..\n'
        #files_list = files.splitlines()
        print('Current path: ' + curpath + '\n')
        choose = input(files)
        print()
        if choose=='..':
            curpath = os.path.dirname(curpath)
            prev = os.path.dirname(curpath)
        else:
            prev = curpath
            curpath = os.path.join(curpath, choose)
        files = ''
        if os.path.isfile(curpath):
            file = open(curpath, 'rb')
            print('Reading file: {}'.format(curpath))
            input('Size = {} bytes'.format(os.path.getsize(curpath)))
            file_read = str(file.read())
            print(file_read)
            if bool(input('Copy file? (press any key then enter for True)')):
                dest_path = asksaveasfilename()
                dest = open(dest_path, 'wb')
                dest.write(str(file_read))
                print('Saved file to: '+dest_path)
                dest.close()
            file.close()
            curpath = prev
            input('Closing file.')
    
except PermissionError:
    print('Permission denied: {}'.format(curpath))
except FileNotFoundError as e:
    print('{}'.format(e))
except KeyboardInterrupt:
    print('Keyboard interrupt')
except UnicodeDecodeError:
    print('File explorer cannot read binary files.')
finally:
    try:
        file.close()
        dest.close()
    except:
        pass
    print('Closed files')
    input('Quitting file explorer')
    print('Written by Matthew Richards')

