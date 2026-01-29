# Написать декоратор log_result, который печатает результат выполнения функции. Применить к функции возведения числа в
# квадрат.
from functools import reduce

def log_result(func):
    def wrapper(*args):
        result = func(*args)
        print(result)
        return result
    return wrapper

@log_result
def some_fun(x):
    return x**2

some_fun(5)

# Написать декоратор repeat(n), который повторяет вызов функции n раз и возвращает последний результат.
def repeat(n):
    def decorator(func):
        def wrapper(*args):
            result = None
            for i in range(n):
                result = func(*args)
            return result
        return wrapper
    return decorator

@repeat(3)
def some_fun1():
    print("Hello")

some_fun1()

# Написать декоратор bench, который измеряет ошибки: если функция завершилась ошибкой, вывести её тип и сообщение.
def bench(func):
    def wrapper(*args):
        result = 0
        try:
            result = func(*args)
        except Exception as e:
            print(func.__name__, type(e).__name__, e)
        return result
    return wrapper

@bench
def some_fun2(x):
    return x // 0

some_fun2(5)

# Дан список слов. Получить список их длин.
lst = list(map(len, ["qwerty", "abc", "lolo", "qwerty123412341234"]))
print(lst)

# Дан список: ['apple', 'Banana', 'cherry', 'DATE']. Получите новый список, оставив только слова в нижнем регистре.
lst = list(filter(lambda x: x.islower(), ['apple', 'Banana', 'cherry', 'DATE']))
print(lst)

# Дан список кортежей (имя, возраст). Получите новый список, оставив кортеж в котором возраст > 18.
lst = list(filter(lambda x: x[1] > 18, [("Ivan", 18), ("Oleg", 25), ("Olya", 10)]))
print(lst)

# Дан список списков: [[1,2], [3,4], [5,6]]. С помощью reduce объединить в один список: [1,2,3,4,5,6].
lst = list(reduce(lambda x, y: x + y, [[1,2], [3,4], [5,6]]))
print(lst)

# Дан список ['cat','car','mouse','dog','snake','cow'].
# Получить словарь: {начальная буква: [слова...]}.
lst = ['cat','car','mouse','dog','snake','cow']
words = set(word[0] for word in lst)
animal_dict = {letter: [word for word in lst if word[0] == letter] for letter in words}
print(animal_dict)

# Дан список кортежей (товар, цена, количество).
# Получить список сумм: цена * количество.
lst = list(map(lambda x: x[1] * x[2], [("Хлеб", 10, 5), ("Молоко", 15, 3)]))
total = reduce(lambda x, y: x + y, lst)
print(lst)
print(total)

















