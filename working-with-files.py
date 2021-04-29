#!/usr/bin/python

# python working-with-files.py

import os
import shutil
import glob

# Source file path
source = 'working-with-files.py'
# Destination file path
destination = source.replace('.py', '_copy.py')

# Print the absolute path to the current directory
print('Current directory absolute path:', os.getcwd())

# List files and directories in the current directory
print(f'Before copying file: {os.listdir()}')

# List all python files in the current directory
py_files = []

for file in glob.glob('*.py'):
    py_files.append(file)

print(f'All .py files: {py_files}')

# Print the absolute path to the source file
print('Absolute path to the source file:', os.path.normpath(os.path.join(
    os.getcwd(), source
)))

# Print file permission of the source
source_perm = oct(os.stat(source).st_mode)[-3:]
print('{file} file permission mode: {perm}\n'.format(
    file=source, perm=source_perm)
)

# Copy the content of source to destination
try:
    dest = shutil.copy(source, destination)
    print('File copied successfully!\n')
# If source and destination are same
except shutil.SameFileError:
    print('Source and destination represents the same file')
# If there is any permission issue
except PermissionError:
    print('Permission denied')
# For other errors
except:
    print('Error occurred while copying file')


# List files and directories in '/home / User / Documents'
print(f'After copying file:\n {os.listdir()}')

# Print file permission of the destination
destination_perm = oct(os.stat(destination).st_mode)[-3:]
print('{file} file permission mode: {perm}'.format(
    file=destination, perm=destination_perm)
)

# Print path of newly created file
print('Destination absolute path:', os.path.abspath(dest))
