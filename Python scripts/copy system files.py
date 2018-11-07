#Copy system files
import os
import sys
import shutils

dest = input('Output path')
shutil.copy(os.path.join('C:', 'Windows', 'System32'), dest)
