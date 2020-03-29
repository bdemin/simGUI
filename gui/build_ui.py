''' Utitily script for building the
UI class py file using pyuic5 '''

import os, fileinput, sys


print('Select which window to build:')
print('1 - main window')
print('2 - results window')

selection = None
while not selection:
    selection = input('Selection: ')
    if selection == '1':
        input_filename = 'main_window.ui'
        output_filename = 'main_window.py'
    elif selection == '2':
        input_filename = 'results_window.ui'
        output_filename = 'results_window.py'
    else:
        print('Invalid selection.')
        selection = None

print('Building Started')

cwd = os.getcwd()
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

# Edit resources import inside the Python file
search_str = 'import resource_file_rc'
replace_str = 'import gui.resources.resources'
for line in fileinput.input('gui/' + output_filename, inplace = 1):
    if search_str in line:
        line = line.replace(search_str, replace_str)
    sys.stdout.write(line)

print('Building Completed')
print('Output file can be found in:', cwd)
