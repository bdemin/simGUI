# Utitily script for building the UI class py file using pyuic5

import os


print('Building Started')

cwd = os.path.join(os.getcwd(), 'gui', 'resources')
input_filename = '\\resource_file.qrc'
input_dir = cwd + input_filename
output_filename = '\\resources.py'
output_dir = cwd + output_filename

username = os.getlogin()
pyside_dir = os.path.join('C:\\Users', username, 'Anaconda3\\Scripts')

command = []
command.append(os.path.join(pyside_dir, 'pyside2-rcc.exe '))
command.append(input_dir + ' ')
command.append('-o ')
command.append(output_dir)

os.system(''.join(command))


print('Building Completed')
print('Output file can be found in:', cwd)
