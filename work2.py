# Базовый класс Animal
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        return "Животное издаёт звук."

    def move(self):
        return "Животное двигается."


# Класс Mammal, наследник Animal
class Mammal(Animal):
    def __init__(self, name, age, hair_color):
        super().__init__(name, age)
        self.hair_color = hair_color

    def feed_milk(self):
        return f"{self.name} кормит детёнышей молоком."

    def make_sound(self):
        return "Млекопитающее издаёт звук."

    def move(self):
        return "Млекопитающее ходит или бегает."


# Класс Bird, наследник Animal
class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span

    def fly(self):
        return f"{self.name} летит, размах крыльев {self.wing_span} м."

    def make_sound(self):
        return "Птица чирикает."

    def move(self):
        return "Птица летает или ходит."


# Класс Fish, наследник Animal
class Fish(Animal):
    def __init__(self, name, age, water_type):
        super().__init__(name, age)
        self.water_type = water_type  # freshwater / saltwater

    def swim(self):
        return f"{self.name} плавает в {self.water_type} воде."

    def make_sound(self):
        return "Рыба не издаёт звуков (или издает пузыри)."

    def move(self):
        return "Рыба плавает."


# Полиморфизм: список разных животных
animals = [
    Mammal("Лев", 5, "золотистый"),
    Bird("Орёл", 3, 2.5),
    Fish("Лосось", 1, "пресной")
]

# Вызов make_sound() и move() для каждого
print("Полиморфизм в действии:")
for animal in animals:
    print(f"{animal.name}:")
    print(f"  Звук: {animal.make_sound()}")
    print(f"  Движение: {animal.move()}")
    print()