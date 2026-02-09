class BankAccount:
    def __init__(self, balance: float = 0):
        self.__balance = balance
        self.daily_limit = 5000
        self.withdrawals_today = 0
        self.count_today_withdrawals = 0
        self.max_withdrawals = 3

    def deposit(self, amount: float):
        if amount <= 0:
            print("Сумма депозита должна быть более 0!")
        self.__balance += amount
        return True

    def withdraw(self, amount: float):
        if amount <= 0:
            print("Сумма снятия должна быть более 0!")
            return False

        if self.count_today_withdrawals == self.max_withdrawals:
            print("На сегодня хватит! Количество снятий = 3")
            return False

        if amount > self.__balance:
            print("Нехватает средств на счету!")
            return False

        if self.withdrawals_today + amount > self.daily_limit:
            print("Суточный лимит исчерпан, сняли более 5000 тысяч!")
            return False

        self.__balance -= amount
        self.withdrawals_today += amount
        self.count_today_withdrawals += 1
        return True



    def get_balance(self):
        return self.__balance

sberbank = BankAccount()
sberbank.deposit(10000)
sberbank.withdraw(100)
sberbank.withdraw(100)
sberbank.withdraw(100)
sberbank.withdraw(100)
print(sberbank.get_balance())
