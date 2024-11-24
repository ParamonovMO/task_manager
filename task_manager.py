from database import DB


class TaskManager:

    def __init__(self):
        self.title = str(input('Введите заголовок задачи: '))
        self.description = str(input('ВВедите описание задачи: '))
        self.status = False
        self.database = DB()
        self.database.create_table_for_db()

    def __str__(self):
        return f"Заголовок задачи: {self.title}, описание задачи: {self.description}, статус задачи {self.status}"

    def __repr__(self):
        return f'Task("{self.title}", "{self.description}")'

    def complete(self):
        if not self.status:
            self.status = True

    def add_task(self):
        self.database.insert_info_to_database(self.title, self.description, self.status)

    def get_tasks(self):
        return self.database.get_info_from_database()

    def update_status_task(self):
        self.database.update_info_to_database(self.status, self.title)

    def del_task(self):
        self.database.delete_task_in_task_manager(self.title)
