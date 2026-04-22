import re

text = "В группе ПИН-231 учатся 19 студентов. В группе ПИН-232 — 22 студента."
pattern = r'[А-Я]+-\d+'
groups = re.findall(pattern, text)
print("Номера групп:", groups)