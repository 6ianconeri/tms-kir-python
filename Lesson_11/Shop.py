# Третье задание
class Shop(object):
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_product_count(self, product):
        return f"{product} - {self.products.count(product)} шт."

    def get_all_products(self):
        return self.products

    def del_product(self, product):
        if product in self.products:
            self.products.remove(product)
            return True
        return False

    def del_all_products(self):
        return self.products.clear()



shop_example = Shop()
shop_example.add_product("Молоко")
shop_example.add_product("Молоко")
shop_example.add_product("Хлеб")
print(shop_example.get_all_products())
print(shop_example.get_product_count("Молоко"))
shop_example.del_product("Молоко")
print(shop_example.products)
shop_example.del_all_products()
print(shop_example.products)


# Реализуйте класс Shop. Предусмотреть возможность работы с произвольным числом продуктов, поиска продуктов по названию
# , добавления их в магазин и удаления продуктов из него.