import re

text = "Это плохое слово, и это тоже плохое"
censored_text = re.sub(r'плохое', '[ЦЕНЗУРА]', text)
print("Исходный текст:", text)
print("Результат замены:", censored_text)