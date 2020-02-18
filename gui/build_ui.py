# Utitily script for building the UI class py file using pyuic5

import os


print('Building Started')

cwd = os.getcwd()
input_filename = 'my_gui.ui'
output_filename = 'main_window.py'


username = os.getlogin() +'\\'
sys_dir = os.path.join('C:\\Users', username)

command = []
command.append('pyuic5 -x ')
command.append(cwd)
command.append('\\gui\\' + input_filename + ' ')
command.append('-o ')
command.append(cwd)
command.append('\\gui\\' + output_filename)

os.system(''.join(command))

print('Building Completed')
print('Output file can be found in:', cwd)
