# Первое задание:
class FirstClass(object):
    def __init__(self, first_var: int = 10, second_var: int = 20):
        self.first_var = first_var
        self.second_var = second_var

    def print_func(self) -> None:
        print(f"Первая переменная - {self.first_var}, Вторая переменная - {self.second_var}")

    def set_first_var(self, first_var: int) -> None:
        self.first_var = first_var

    def set_second_var(self, second_var: int) -> None:
        self.second_var = second_var

    def sum_func(self) -> None:
        print(f"Сумма равна: {self.first_var + self.second_var}")

    def what_is_more_func(self) -> None:
        if self.first_var > self.second_var:
            print(f"Первая больше - {self.first_var}, чем вторая - {self.second_var}")
        elif self.first_var < self.second_var:
            print(f"Вторая больше - {self.second_var}, чем первая - {self.first_var}")
        else:
            print("Равны!")

example_class = FirstClass()
example_class.print_func()
example_class.set_first_var(100)
example_class.set_second_var(200)
example_class.print_func()
example_class.sum_func()
example_class.what_is_more_func()