from datetime import datetime

def format_date(date_obj):
    # Русские названия месяцев
    months_ru = [
        "января", "февраля", "марта", "апреля", "мая", "июня",
        "июля", "августа", "сентября", "октября", "ноября", "декабря"
    ]
    # Английские сокращения месяцев
    months_en_short = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                       "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    
    day = date_obj.day
    month_ru = months_ru[date_obj.month - 1]
    year = date_obj.year
    
    # 1. "10 апреля 2026 года"
    format1 = f"{day} {month_ru} {year} года"
    
    # 2. "10.04.2026"
    format2 = date_obj.strftime("%d.%m.%Y")
    
    # 3. "2026-04-10"
    format3 = date_obj.strftime("%Y-%m-%d")
    
    # 4. "Apr 10, 2026"
    month_en = months_en_short[date_obj.month - 1]
    format4 = f"{month_en} {day:02d}, {year}"
    
    return format1, format2, format3, format4

# Пример вызова
date_input = input("Введите дату в формате ДД.ММ.ГГГГ: ")
date_obj = datetime.strptime(date_input, "%d.%m.%Y").date()

formats = format_date(date_obj)
print(formats[0])
print(formats[1])
print(formats[2])
print(formats[3])