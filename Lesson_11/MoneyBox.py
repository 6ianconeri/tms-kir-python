# Реализуйте класс MoneyBox, для работы с виртуальной копилкой. Каждая копилка имеет ограниченную вместимость, которая
# выражается целым числом – количеством монет(capacity -вместимость), которые можно положить в копилку. Класс должен
# поддерживать информацию о количестве монет в копилке, предоставлять возможность добавлять монеты в копилку и узнавать,
# можно ли добавить в копилку ещё какое-то количество монет, не превышая ее вместимость.

class MoneyBox:
    def __init__(self, capacity: int = 10, money: int = 0):
        self.capacity = capacity
        self.money = money

    def can_add_money(self, money_to_add: int) -> bool:
        return money_to_add + self.money <= self.capacity

    def add_money(self, money_to_add: int):
        if self.can_add_money(money_to_add):
            self.money += money_to_add
            return f"Положили {money_to_add} монет, осталось места на {self.capacity - self.money} монет"
        return f"Нет места, положите меньше!"

    def get_capacity(self):
        return f"Размер копилки - {self.capacity}"

    def get_count_money(self):
        return f"В копилке сейчас - {self.money} монет"


money_box_1 = MoneyBox()
print(money_box_1.can_add_money(10))
print(money_box_1.add_money(8))
print(money_box_1.can_add_money(3))
print(money_box_1.get_capacity())
print(money_box_1.get_count_money())
print(money_box_1.can_add_money(2))
print(money_box_1.add_money(2))





