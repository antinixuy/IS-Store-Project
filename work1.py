# Базовый класс Employee
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        return f"{self.name} выполняет общую работу."

    def get_info(self):
        return f"Имя: {self.name}, Зарплата: {self.salary}"


# Класс Developer, наследник Employee
class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def write_code(self):
        return f"{self.name} пишет код на {self.programming_language}."

    # Переопределение метода work()
    def work(self):
        return f"{self.name} разрабатывает программное обеспечение на {self.programming_language}."

    # Расширение метода get_info()
    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Язык программирования: {self.programming_language}"


# Класс Designer, наследник Employee
class Designer(Employee):
    def __init__(self, name, salary, software):
        super().__init__(name, salary)
        self.software = software

    def design(self):
        return f"{self.name} создаёт дизайн в {self.software}."

    def work(self):
        return f"{self.name} занимается дизайном с использованием {self.software}."

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, ПО для дизайна: {self.software}"


# Класс Manager, наследник Employee
class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def manage(self):
        return f"{self.name} управляет командой из {self.team_size} человек."

    def work(self):
        return f"{self.name} координирует работу команды из {self.team_size} человек."

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Размер команды: {self.team_size}"


# Создание списка сотрудников
employees = [
    Developer("Алексей", 120000, "Python"),
    Designer("Мария", 95000, "Figma"),
    Manager("Олег", 150000, 5)
]

# Вывод информации и работы каждого сотрудника
for emp in employees:
    print(emp.get_info())
    print(emp.work())
    print("-" * 30)

# Дополнительно: вызов специфических методов, если нужно
print(employees[0].write_code())
print(employees[1].design())
print(employees[2].manage())