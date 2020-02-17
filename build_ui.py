# Utitily script for building the UI class py file using pyuic5

import os


print('Building Started')

cwd = os.getcwd()
input_ui_file = 'untitled.ui'

username = os.getlogin() +'\\'
sys_dir = os.path.join('C:\\Users', username)
os.system('cd ' + sys_dir)

console_cmd = os.path.join('pyuic5 -x ' + cwd, input_ui_file + ' -o ' + cwd, 'output.py')
os.system(console_cmd)

print('Building Completed')
print('Output file can be found in:', cwd)
