from mypackage.models.student import Student
from mypackage.utils.validators import validate_student_name
from mypackage.api.client import get_random_quote  # предполагается наличие

def interactive_mode():
    while True:
        print("\nМеню:")
        print("1. Создать студента")
        print("2. Добавить оценки")
        print("3. Показать студента")
        print("4. Получить случайную цитату")
        print("5. Показать случайную цитату (из уже загруженного API)")
        print("0. Выход")
        choice = input("Выберите пункт: ")

        if choice == "1":
            first = input("Имя: ")
            last = input("Фамилия: ")
            age = int(input("Возраст: "))
            is_valid, msg = validate_student_name(first, last)
            if is_valid:
                student = Student(first, last, age)
                print("Студент создан.")
            else:
                print(f"Ошибка: {msg}")

        elif choice == "2":
            # пример добавления оценок
            pass

        elif choice == "3":
            # пример вывода студента
            pass

        elif choice == "4":
            quote = get_random_quote()
            print(f"Цитата: {quote}")

        elif choice == "5":
            quote = get_random_quote()
            print(f"Случайная цитата: {quote['content']} — {quote['author']}")

        elif choice == "0":
            break
        else:
            print("Неверный ввод.")