from datetime import date, timedelta, datetime   # <-- обязательно добавьте datetime

def calculate_age(birth_date):
    today = date.today()
    
    # Вычисляем базовый возраст в годах
    age_years = today.year - birth_date.year
    
    # Проверяем, был ли уже день рождения в этом году
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age_years -= 1
        last_birthday = date(today.year - 1, birth_date.month, birth_date.day)
    else:
        last_birthday = date(today.year, birth_date.month, birth_date.day)
    
    days_since_birthday = (today - last_birthday).days
    months = days_since_birthday // 30
    days = days_since_birthday % 30
    
    next_birthday = date(today.year, birth_date.month, birth_date.day)
    if next_birthday < today:
        next_birthday = date(today.year + 1, birth_date.month, birth_date.day)
    
    days_until_next_birthday = (next_birthday - today).days
    
    return age_years, months, days, days_until_next_birthday

# Ввод даты рождения
birth_input = input("Введите дату рождения в формате ДД.ММ.ГГГГ: ")
birth_date = datetime.strptime(birth_input, "%d.%m.%Y").date()   # теперь datetime определён

years, months, days, until_next = calculate_age(birth_date)
print(f"Возраст: {years} лет, {months} месяцев, {days} дней")
print(f"До следующего дня рождения осталось {until_next} дней")