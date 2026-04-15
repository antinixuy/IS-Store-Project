from datetime import datetime, timedelta

class TaskPlanner:
    def __init__(self):
        self.tasks = []  # список словарей: {'title': str, 'due_date': date}
    
    def add_task(self, title, due_date_str):
        due_date = datetime.strptime(due_date_str, "%d.%m.%Y").date()
        self.tasks.append({'title': title, 'due_date': due_date})
    
    def get_tasks_today(self):
        today = datetime.now().date()
        return [task for task in self.tasks if task['due_date'] == today]
    
    def get_overdue_tasks(self):
        today = datetime.now().date()
        return [task for task in self.tasks if task['due_date'] < today]
    
    def get_tasks_next_week(self):
        today = datetime.now().date()
        next_week = today + timedelta(days=7)
        return [task for task in self.tasks if today <= task['due_date'] <= next_week]

# Пример использования
planner = TaskPlanner()
planner.add_task("Сдать отчёт", "10.04.2026")
planner.add_task("Купить продукты", "09.04.2026")
planner.add_task("Позвонить врачу", "05.04.2026")
planner.add_task("Оплатить счета", "15.04.2026")

print("Задачи на сегодня:")
for task in planner.get_tasks_today():
    print(f" - {task['title']}")

print("\nПросроченные задачи:")
for task in planner.get_overdue_tasks():
    print(f" - {task['title']} (дата: {task['due_date'].strftime('%d.%m.%Y')})")

print("\nЗадачи на ближайшие 7 дней:")
for task in planner.get_tasks_next_week():
    print(f" - {task['title']} (дата: {task['due_date'].strftime('%d.%m.%Y')})")