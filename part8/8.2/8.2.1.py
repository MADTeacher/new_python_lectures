import pathlib

# Создание каталога
pathlib.Path('my_directory').mkdir(exist_ok=True)
print('Каталог создан')

# Удаление каталога
pathlib.Path('my_directory').rmdir()
print('Каталог удален')
