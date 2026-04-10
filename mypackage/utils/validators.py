def validate_student_name(first_name, last_name):
    def is_valid_name(name):
        return name and name.istitle() and name.replace('-', '').isalpha()

    if not is_valid_name(first_name):
        return False, "Имя должно начинаться с заглавной буквы и содержать только буквы или дефис."
    if not is_valid_name(last_name):
        return False, "Фамилия должна начинаться с заглавной буквы и содержать только буквы или дефис."
    return True, "Имя и фамилия корректны."