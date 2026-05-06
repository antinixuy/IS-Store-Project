import random
import time
import bisect

# Создаём список из 1 000 000 случайных чисел
print("Генерация 1 000 000 случайных чисел...")
data = [random.randint(1, 1_000_000) for _ in range(1_000_000)]

# Выбираем случайное число, которое точно есть в списке
target = random.choice(data)
print(f"Искомое число: {target}")

# Линейный поиск
print("\n--- Линейный поиск ---")
start = time.perf_counter()
linear_index = -1
for i, val in enumerate(data):
    if val == target:
        linear_index = i
        break
elapsed_linear = time.perf_counter() - start
print(f"Индекс: {linear_index}")
print(f"Время: {elapsed_linear:.6f} сек")

# Сортировка
print("\n--- Сортировка ---")
start = time.perf_counter()
data.sort()
elapsed_sort = time.perf_counter() - start
print(f"Время сортировки: {elapsed_sort:.6f} сек")

# Бинарный поиск
print("\n--- Бинарный поиск ---")
start = time.perf_counter()
binary_index = bisect.bisect_left(data, target)
if binary_index < len(data) and data[binary_index] == target:
    pass
else:
    binary_index = -1
elapsed_binary = time.perf_counter() - start
print(f"Индекс: {binary_index}")
print(f"Время: {elapsed_binary:.6f} сек")

# Сравнение
print("\n--- Сравнение ---")
print(f"Линейный поиск: {elapsed_linear:.6f} сек")
print(f"Бинарный поиск: {elapsed_binary:.6f} сек")
print(f"Бинарный поиск быстрее в {elapsed_linear / elapsed_binary:.2f} раз")