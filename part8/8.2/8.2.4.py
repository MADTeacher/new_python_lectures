import os

directory_path = '/path/to/directory'

# получение списка файлов и каталогов
directory_contents = os.listdir(directory_path)

# вывод содержимого директории
print(f"Содержимое директории {directory_path}:")
for content in directory_contents:
    print(content)
