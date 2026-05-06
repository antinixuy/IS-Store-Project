import random
import time

def bubble_sort(arr):
    """Сортировка пузырьком (возвращает отсортированную копию)."""
    a = arr.copy()
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a

# Создаём список из 10 000 случайных чисел
size = 10_000
print(f"Генерация {size} случайных чисел...")
data = [random.randint(1, 1_000_000) for _ in range(size)]

# Сортировка пузырьком
print("\n--- Сортировка пузырьком ---")
start = time.perf_counter()
sorted_bubble = bubble_sort(data)
elapsed_bubble = time.perf_counter() - start
print(f"Время: {elapsed_bubble:.6f} сек")

# Встроенная сортировка
print("\n--- Встроенная сортировка ---")
start = time.perf_counter()
sorted_builtin = sorted(data)
elapsed_builtin = time.perf_counter() - start
print(f"Время: {elapsed_builtin:.6f} сек")

# Сравнение
print("\n--- Сравнение ---")
print(f"Пузырьковая сортировка: {elapsed_bubble:.6f} сек")
print(f"Встроенная сортировка: {elapsed_builtin:.6f} сек")
print(f"Встроенная быстрее в {elapsed_bubble / elapsed_builtin:.2f} раз")