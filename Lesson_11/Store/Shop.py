class Shop(object):
    def __init__(self):
        self.products = {}

class Stock:
    def __init__(self):
        self.products = ['Молоко', 'Хлеб']

class Seller:
    def add_product(self, product, price, shop, stock):
        if product in stock.products:
            stock.products.remove(product)
            shop.products[product] = price

class Client:
    def __init__(self, money):
        self.money = money

    def buy_product(self, product, shop):
        if product in shop.products:
            if self.money >= shop.products[product]:
                self.money -= shop.products[product]
                del shop.products[product]
            else:
                return f"Увы, средств не хватает..."
        else:
            price = int(input("Продавец выставляет стоимость: "))
            seller.add_product(product, price, shop, stock)
            if product in shop.products:
                if self.money >= shop.products[product]:
                    self.money -= shop.products[product]
                    del shop.products[product]
                else:
                    return f"Товар привезли, но нехватает средств."
            else:
                return f"Товара нет даже на складе!"
        return f"Товар '{product}' успешно куплен! Осталось {self.money} р."

    def get_money(self):
        return self.money





shop = Shop()
client = Client(300)
seller = Seller()
stock = Stock()
seller.add_product("Молоко", 100, shop, stock)
print(shop.products)
print(client.buy_product("Хлеб", shop))
print(client.get_money())
print(shop.products)
