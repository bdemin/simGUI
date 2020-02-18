# Utitily script for building the UI class py file using pyuic5

import os


print('Building Started')

cwd = os.getcwd()
input_filename = 'resource_file.qrc'
input_dir = cwd + '\\resources\\'
output_filename = 'resources.py'
output_dir = cwd + '\\resources\\'

username = os.getlogin()
pyside_dir = os.path.join('C:\\Users', username, 'Anaconda3\\Lib\\site-packages\\PySide2')
os.system('cd ' + pyside_dir)

command = []
command.append('pyside2-rcc.exe ')
command.append(input_dir)
command.append(input_filename + ' ')
command.append('-o ')
command.append(output_dir)
command.append(output_filename)

os.system(''.join(command))

print('Building Completed')
print('Output file can be found in:', cwd)
