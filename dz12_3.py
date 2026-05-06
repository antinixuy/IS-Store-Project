import time
from dataclasses import dataclass

@dataclass
class Student:
    name: str
    group: str
    avg_score: float

    def __repr__(self):
        return f"{self.name} ({self.group}, ср.балл {self.avg_score})"

def linear_search_by_name(students, target_name):
    """Линейный поиск студента по имени."""
    for student in students:
        if student.name.lower() == target_name.lower():
            return student
    return None

def binary_search_by_score(students, target_score):
    """Бинарный поиск студента по среднему баллу (список должен быть отсортирован)."""
    left, right = 0, len(students) - 1
    while left <= right:
        mid = (left + right) // 2
        if students[mid].avg_score == target_score:
            return students[mid]
        elif students[mid].avg_score < target_score:
            left = mid + 1
        else:
            right = mid - 1
    return None

# Список студентов
students = [
    Student("Иванов Иван", "ПИН-231", 4.5),
    Student("Петрова Анна", "ПИН-232", 4.8),
    Student("Сидоров Сергей", "ПИН-231", 3.9),
    Student("Кузнецова Мария", "ПИН-233", 4.2),
    Student("Васильев Дмитрий", "ПИН-232", 3.7),
    Student("Попова Елена", "ПИН-231", 5.0),
    Student("Смирнов Алексей", "ПИН-233", 4.1),
]

print("Список студентов:")
for s in students:
    print(f"  {s}")

# Поиск по имени (линейный)
search_name = "Кузнецова Мария"
print(f"\n--- Поиск по имени: '{search_name}' ---")
start = time.perf_counter()
found = linear_search_by_name(students, search_name)
elapsed_linear = time.perf_counter() - start
print(f"Результат: {found}")
print(f"Время: {elapsed_linear:.6f} сек")

# Поиск по среднему баллу (бинарный) – сначала сортируем
students_sorted = sorted(students, key=lambda s: s.avg_score)
print("\nСтуденты, отсортированные по среднему баллу:")
for s in students_sorted:
    print(f"  {s}")

target_score = 4.2
print(f"\n--- Поиск по среднему баллу: {target_score} ---")
start = time.perf_counter()
found_score = binary_search_by_score(students_sorted, target_score)
elapsed_binary = time.perf_counter() - start
print(f"Результат: {found_score}")
print(f"Время: {elapsed_binary:.6f} сек")

print("\n--- Сравнение времени ---")
print(f"Линейный поиск по имени: {elapsed_linear:.6f} сек")
print(f"Бинарный поиск по баллам: {elapsed_binary:.6f} сек")