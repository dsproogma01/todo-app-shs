
class TaskManager:
    def __init__(self):
        self.__tasks = []
    def add_task(self, title, description):
        self.__tasks.append({"title": title, "description": description, "done": False})
    def remove_task(self, title):
        self.__tasks = [task for task in self.__tasks if task['title'] != title]
    def mark_as_done(self, title):
        for task in self.__tasks:
            if task['title'] == title:
                task['done'] = True
                break

    def show_tasks(self):
        if not self.__tasks:
            print("Задач для выполнения нема")
        else:
            for task in self.__tasks:
                status = "Выполнено" if task['done'] else "Не выполнено"
                print(f"Задача: {task['title']} \nОписание: {task['description']} \nСтатус: {status}\n")

    def __str__(self):
        return f"Количество задач: {len(self.__tasks)}"

if __name__ == '__main__':
    task_manager = TaskManager()
    task_manager.add_task("Купить продукты", "Купить молоко, хлеб, яйца ")
    task_manager.add_task("Пойти на игру ",  "забить как можно больше голов")

    task_manager.mark_as_done("Купить продукты")
    task_manager.show_tasks()


    task_manager.remove_task("Купить продукты")
    task_manager.show_tasks()

