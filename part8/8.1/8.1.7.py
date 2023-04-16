import shutil

src_file = '/path/to/source/file.txt'
dst_file = '/path/to/destination/file.txt'

try:
    shutil.copy(src_file, dst_file)
    print('Файл успешно скопирован!')
except FileNotFoundError:
    print(f'Ошибка: файл {src_file} не найден')
except IsADirectoryError:
    print(f'Ошибка: {src_file} - это директория, а не файл')
except PermissionError:
    print(f'Ошибка: нет доступа к файлу {src_file}')
except Exception as e:
    print(f'Ошибка: {e}')
