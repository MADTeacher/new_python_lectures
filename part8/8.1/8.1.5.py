import os

file_path = '/path/to/file.txt'

if os.path.isfile(file_path):
    print(f'Файл {file_path} существует.')
else:
    print(f'Файл {file_path} не найден.')
