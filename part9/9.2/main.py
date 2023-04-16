import os

from database import DB_NAME
from database.create_db import create_db
from menu.main import create_main_menu

if __name__ == '__main__':
    if not os.path.exists(DB_NAME):
        create_db()
    create_main_menu()
