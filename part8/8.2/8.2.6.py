import os

directory_path = '/path/to/directory'

# переход в директорию
os.chdir(directory_path)
print(f"Текущая директория: {os.getcwd()}")
