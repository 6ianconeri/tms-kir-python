# Второе задание:
class DecimalCounter(object):
    def __init__(self, count: int = 10):
        self.count = count

    def count_up(self):
        self.count += 1
        return self.count

    def count_down(self):
        self.count -= 1
        return self.count

    def show_count(self):
        return self.count

example_class = DecimalCounter()
print(example_class.show_count())
example_class.count_up()
print(example_class.show_count())
example_class.count_up()
print(example_class.show_count())
example_class.count_down()
print(example_class.show_count())