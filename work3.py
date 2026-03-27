# Базовый класс Notifier
class Notifier:
    def send(self, message):
        raise NotImplementedError("Метод send должен быть переопределён в наследнике")


# Класс EmailNotifier
class EmailNotifier(Notifier):
    def __init__(self, email_address):
        self.email_address = email_address

    def send(self, message):
        # Здесь могла бы быть реальная отправка email
        return f"Отправка email на {self.email_address}: {message}"


# Класс SMSNotifier
class SMSNotifier(Notifier):
    def __init__(self, phone_number):
        self.phone_number = phone_number

    def send(self, message):
        # Здесь могла бы быть реальная отправка SMS
        return f"Отправка SMS на {self.phone_number}: {message}"


# Класс PushNotifier
class PushNotifier(Notifier):
    def __init__(self, device_token):
        self.device_token = device_token

    def send(self, message):
        # Здесь могла бы быть реальная отправка push-уведомления
        return f"Отправка push-уведомления на устройство {self.device_token}: {message}"


# Полиморфная функция для отправки сообщения всем notifier'ам
def notify_all(notifiers, message):
    results = []
    for notifier in notifiers:
        results.append(notifier.send(message))
    return results


# Демонстрация работы
notifiers = [
    EmailNotifier("user@example.com"),
    SMSNotifier("+7 123 456-78-90"),
    PushNotifier("device_token_12345")
]

message = "Внимание! Система обновляется в 23:00."
results = notify_all(notifiers, message)

print("Результаты отправки уведомлений:")
for result in results:
    print(result)