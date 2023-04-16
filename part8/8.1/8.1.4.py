import os

file_path = '/path/to/file.txt'

try:
    os.remove(file_path)
    print('Файл успешно удален!')
except FileNotFoundError:
    print(f'Файл {file_path} не найден.')
except PermissionError:
    print(f'Нет разрешения на удаление файла {file_path}.')
except Exception as e:
    print(f'Ошибка при удалении файла {file_path}: {e}')
