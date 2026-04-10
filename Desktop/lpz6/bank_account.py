class BankAccount:

    def __init__(self, account_number, owner, balance=0, currency="RUB"):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
        self.currency = currency

    def deposit(self, amount):
        self.balance += amount
        print("Пополнение:", amount, self.currency)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Недостаточно средств")
        else:
            self.balance -= amount
            print("Снятие:", amount, self.currency)

    def get_balance(self):
        return self.balance

    def display_info(self):
        print("Номер счета:", self.account_number)
        print("Владелец:", self.owner)
        print("Баланс:", self.balance, self.currency)


# пример использования
account = BankAccount("12345", "Amir", 1000)

account.display_info()
account.deposit(500)
account.withdraw(200)

print("Текущий баланс:", account.get_balance())