from task_manager import TaskManager

if __name__ == '__main__':
    while True:
        question = input('Что вы хотите? ')
        if question == 'Создать таск': 
            task = TaskManager()
            task.add_task()
        question = input('Что вы хотите? ')
        if question == 'Напечатать':
            print(task)
        question = input('Что вы хотите? ')
        if question == 'Получить записи':   
            task.get_tasks()
        question = input('Что вы хотите? ')
        if question == 'Выполнено':
            task.complete()
            task.update_status_task()
        question = input('Что вы хотите? ')
        if question == 'Выйти':
            break
