class SpaceSection:
    """Класс космического отсека с защищёнными параметрами."""

    def __init__(self, name, oxygen, temperature, pressure, access_code):
        self.name = name                     # публичное название отсека
        self.__oxygen_level = oxygen          # уровень кислорода (0-100)
        self.__temperature = temperature      # температура (-50..+50)
        self.__pressure = pressure            # давление (0.5..2.0 атм)
        self.__access_code = str(access_code) # код доступа (строка из 4 цифр)
        self.__captain_password = "admin123"  # секретный пароль капитана

    # ---------- Геттеры (доступ без пароля для параметров) ----------
    def get_oxygen(self):
        return f"Кислород в {self.name}: {self.__oxygen_level}%"

    def get_temperature(self):
        return f"Температура в {self.name}: {self.__temperature}°C"

    def get_pressure(self):
        return f"Давление в {self.name}: {self.__pressure} атм"

    # Геттер для кода доступа – требует пароль капитана
    def get_access_code(self, password):
        if password == self.__captain_password:
            return f"Код доступа к {self.name}: {self.__access_code}"
        else:
            return "🔒 Доступ запрещён! Неверный пароль."

    # ---------- Сеттеры с проверкой диапазонов ----------
    def set_oxygen(self, level):
        if 0 <= level <= 100:
            self.__oxygen_level = level
            print(f"✅ Уровень кислорода в {self.name} изменён на {level}%")
        else:
            print("❌ Ошибка! Кислород должен быть от 0 до 100")

    def set_temperature(self, temp):
        if -50 <= temp <= 50:
            self.__temperature = temp
            print(f"✅ Температура в {self.name} изменена на {temp}°C")
        else:
            print("❌ Ошибка! Температура должна быть от -50 до +50")

    def set_pressure(self, pressure):
        if 0.5 <= pressure <= 2.0:
            self.__pressure = pressure
            print(f"✅ Давление в {self.name} изменено на {pressure} атм")
        else:
            print("❌ Ошибка! Давление должно быть в пределах 0.5–2.0 атм")

    # Смена кода доступа (с подтверждением старого и проверкой формата)
    def set_access_code(self, old_code, new_code):
        if old_code == self.__access_code:
            new_code_str = str(new_code)
            if len(new_code_str) == 4 and new_code_str.isdigit():
                self.__access_code = new_code_str
                print(f"✅ Код доступа к {self.name} успешно изменён")
            else:
                print("❌ Новый код должен состоять ровно из 4 цифр!")
        else:
            print("❌ Неверный текущий код доступа!")

    # ---------- Аварийный отчёт (только для капитана) ----------
    def emergency_report(self, password):
        if password == self.__captain_password:
            print("\n" + "=" * 45)
            print(f"🚨 АВАРИЙНЫЙ ОТЧЁТ: {self.name}")
            print(f"   Кислород : {self.__oxygen_level}%")
            print(f"   Температура: {self.__temperature}°C")
            print(f"   Давление  : {self.__pressure} атм")
            print(f"   Код доступа: {self.__access_code}")
            print("=" * 45)
        else:
            print("👁 Только капитан может просматривать аварийные отчёты!")


# ---------- Бонус: класс космического корабля ----------
class Spaceship:
    """Корабль, содержащий несколько отсеков."""

    def __init__(self):
        # Создаём три отсека с разными параметрами
        self.sections = [
            SpaceSection("Жилой отсек", 75, 22, 1.0, "1234"),
            SpaceSection("Двигательный отсек", 85, 150, 1.8, "5678"),  # температура за пределами!
            SpaceSection("Научный отсек", 70, 18, 0.9, "9012")
        ]

    def check_all_systems(self):
        """Автоматическая проверка всех параметров каждого отсека."""
        print("\n" + "=" * 55)
        print("🔍 ПРОВЕРКА ВСЕХ СИСТЕМ КОРАБЛЯ")
        print("=" * 55)
        for section in self.sections:
            print(f"\n--- {section.name} ---")
            print(section.get_oxygen())
            print(section.get_temperature())
            print(section.get_pressure())

            # Дополнительная проверка нахождения параметров в норме
            warnings = []
            if not (0 <= section._SpaceSection__oxygen_level <= 100):
                warnings.append("Кислород вне допустимого диапазона!")
            if not (-50 <= section._SpaceSection__temperature <= 50):
                warnings.append("Температура вне допустимого диапазона!")
            if not (0.5 <= section._SpaceSection__pressure <= 2.0):
                warnings.append("Давление вне допустимого диапазона!")

            if warnings:
                print("⚠️  ПРЕДУПРЕЖДЕНИЯ:")
                for w in warnings:
                    print(f"   - {w}")
            else:
                print("✅ Все параметры в норме.")
        print("=" * 55)


# ---------- Демонстрация работы ----------
if __name__ == "__main__":
    print("🚀 ЗАПУСК СИСТЕМЫ КОСМИЧЕСКОГО КОРАБЛЯ")
    print("=" * 50)

    # Создаём командный отсек
    command_section = SpaceSection("Командный отсек", 80, 21, 1.2, "4321")

    # Начальное состояние
    print("\n📊 НАЧАЛЬНОЕ СОСТОЯНИЕ:")
    print(command_section.get_oxygen())
    print(command_section.get_temperature())
    print(command_section.get_pressure())

    # Проверка доступа к коду
    print("\n🔑 ПРОВЕРКА ДОСТУПА:")
    print(command_section.get_access_code("wrong"))
    print(command_section.get_access_code("admin123"))

    # Изменение параметров
    print("\n⚙️ ИЗМЕНЕНИЕ ПАРАМЕТРОВ:")
    command_section.set_oxygen(95)
    command_section.set_temperature(100)   # ошибка (вне диапазона)
    command_section.set_pressure(2.5)      # ошибка (вне диапазона)
    command_section.set_pressure(1.5)      # успешно

    # Смена кода доступа
    print("\n🔐 СМЕНА КОДА ДОСТУПА:")
    command_section.set_access_code("4321", "9999")   # правильно
    command_section.set_access_code("9999", "777")    # ошибка (не 4 цифры)

    # Аварийный отчёт
    print("\n📢 АВАРИЙНЫЙ ОТЧЁТ:")
    command_section.emergency_report("user123")       # неверный пароль
    command_section.emergency_report("admin123")      # верный пароль

    # Проверка всего корабля
    print("\n🛰 БОНУС: ПРОВЕРКА КОРАБЛЯ")
    spaceship = Spaceship()
    spaceship.check_all_systems()