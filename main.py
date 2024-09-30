class ToDoList:
    def __init__(self):
        self.tasks = {}  # Store tasks as a dictionary with task_id as the key

    def add_task(self, description):
        task_id = len(self.tasks) + 1
        self.tasks[task_id] = {'description': description, 'status': 'Не начата'}
        print(f"Задача добавлена: {task_id} - {description}")

    def remove_task(self, task_id):
        if task_id in self.tasks:
            removed_task = self.tasks.pop(task_id)
            print(f"Задача удалена: {task_id} - {removed_task['description']}")
        else:
            print("Задача с таким ID не найдена.")

    def update_status(self, task_id, status):
        if task_id in self.tasks:
            if status in ["Не начата", "В процессе", "Завершена"]:
                self.tasks[task_id]['status'] = status
                print(f"Статус задачи {task_id} изменён на '{status}'")
            else:
                print("Недопустимый статус. Выберите один из: 'Не начата', 'В процессе', 'Завершена'.")
        else:
            print("Задача с таким ID не найдена.")

    def view_tasks(self):
        if not self.tasks:
            print("Список задач пуст.")
        else:
            print("Текущие задачи:")
            for task_id, details in self.tasks.items():
                print(f"{task_id}. {details['description']} - Статус: {details['status']}")

    def save_to_file(self, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            for task_id, details in self.tasks.items():
                f.write(f"{task_id},{details['description']},{details['status']}\n")
        print(f"Задачи сохранены в файл {filename}")

    def load_from_file(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                self.tasks.clear()
                for line in f:
                    task_id, description, status = line.strip().split(',')
                    self.tasks[int(task_id)] = {'description': description, 'status': status}
            print(f"Задачи загружены из файла {filename}")
        except FileNotFoundError:
            print(f"Файл {filename} не найден.")


def main():
    todo_list = ToDoList()

    # Добавление нескольких задач
    todo_list.add_task("Написать отчёт")
    todo_list.add_task("Сходить в магазин")
    todo_list.add_task("Позвонить другу")

    # Изменение статуса задачи
    todo_list.update_status(2, "В процессе")

    # Удаление задачи
    todo_list.remove_task(1)

    # Отображение списка задач
    todo_list.view_tasks()

    # Сохранение списка задач в файл
    todo_list.save_to_file('todo_list.txt')

    # Загрузка списка задач из файла
    todo_list.load_from_file('todo_list.txt')
    todo_list.view_tasks()


if __name__ == "__main__":
    main()
