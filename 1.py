# lambda-функции для калькулятора
subtract = lambda a, b: a - b
modulus = lambda a, b: a % b
power = lambda a, b: a ** b
is_positive = lambda a: a > 0

# Проверка
print("Вычитание:", subtract(10, 3))
print("Остаток от деления:", modulus(10, 3))
print("Степень:", power(2, 3))
print("Число положительное:", is_positive(-5))