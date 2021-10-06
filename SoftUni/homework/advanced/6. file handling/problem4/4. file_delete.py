import os

file_path = 'test.txt'
if os.path.exists(file_path):
    os.remove(file_path)
else:
    print('File already deleted!')

try:
    os.remove('asd.txt')
except FileNotFoundError:
    print('File already deleted!')