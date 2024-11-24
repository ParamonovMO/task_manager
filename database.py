import logging
import sqlite3

logging.basicConfig(
    filename='logs.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


class DB:
    def __init__(self):
        self.database = 'DB.db'

    def create_table_for_db(self):
        with sqlite3.connect(self.database) as connect:
            connect.execute("""
                            CREATE TABLE IF NOT EXISTS task_manager
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            title TEXT,
                            description TEXT,
                            status INTEGER
                            )
                        """)
        logging.info('Создана или проверена таблица')

    def get_info_from_database(self):
        with sqlite3.connect(self.database) as connect:
            return list(connect.execute('SELECT * from task_manager'))

    def insert_info_to_database(self, title, description, status):
        with sqlite3.connect(self.database) as connect:
            connect.execute('INSERT INTO task_manager (title, description, status) VALUES (?, ?, ?)', (title, description, status))
            connect.commit()
        logging.info('Запись в базу данных')

    def update_info_to_database(self, status, title):
        with sqlite3.connect(self.database) as connect:
            connect.execute('UPDATE task_manager SET status = ? WHERE title = ?', (status, title))
            connect.commit()
        logging.info('Обновление записи')

    def delete_task_in_task_manager(self, title):
        with sqlite3.connect(self.database) as connect:
            connect.execute(f'DELETE from task_manager WHERE {title}')
            connect.commit()
        logging.info('Обновление записи')
