import re

def check_phone(phone):
    pattern = r'^\+7-\d{3}-\d{3}-\d{2}-\d{2}$'
    return bool(re.match(pattern, phone))

user_phone = input("Введите номер телефона в формате +7-999-123-45-67: ")
if check_phone(user_phone):
    print("Номер корректен.")
else:
    print("Номер не соответствует формату.")