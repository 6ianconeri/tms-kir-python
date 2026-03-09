from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CardPaymentMethod(PaymentMethod):
    def pay(self, amount):
        print(f"С Вас {amount}")
        print("Вставьте карту")
        input("Введите пин-код: ")
        print(f"Оплата картой успешно проведена, оплачено: {amount}")

class CashPaymentMethod(PaymentMethod):
    def pay(self, amount):
        print(f"С Вас {amount}")
        print(f"Оплата наличными успешно проведена, оплачено: {amount}")

class QRPaymentMethod(PaymentMethod):
    def pay(self, amount):
        print(f"С Вас {amount}")
        print("Наведите камеру телефона на QR-код")
        print(f"Оплата QR-кодом успешно проведена, оплачено: {amount}")

card = CardPaymentMethod()
cash = CashPaymentMethod()
qr = QRPaymentMethod()

card.pay(100)
cash.pay(100)
qr.pay(100)