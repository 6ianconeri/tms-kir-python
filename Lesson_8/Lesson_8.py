# Опишите конструкцию отлова ошибок, так чтобы выводило, какую ошибку вы сделали. Код представлен ниже:
# x = (1, 2, 5, 7)
# x = x  / 2
# print(x)
try:
    x = (1, 2 , 5, 7)
    x = x / 2
    print(x)
except TypeError:
    print("TypeError")

# Напишите программу, которая будет ловить IndexError когда вы пытаетесь взять индекс элемента, которого нет в списке.
x = [1, 2, 3, 4, 5]
try:
    print(x[10])
except IndexError:
    print("IndexError")

# Напишите программу, которая вычисляет площадь треугольника по формуле Герона, однако если пользователь введёт длину
# хоть одной стороны треугольника равную 0, то программа должна бросить исключение ArithmeticError.
try:
    a = int(input("Введите первую сторону треугольника: "))
    b = int(input("Введите вторую сторону треугольника: "))
    c = int(input("Введите третью сторону треугольника: "))
    if a == 0 or b == 0 or c == 0:
        raise ArithmeticError
    semiperimeter = (a + b + c) / 2
    square = (semiperimeter * (semiperimeter - a) * (semiperimeter - b) * (semiperimeter - c)) ** 0.5
    print(square)
except ArithmeticError:
    print("ArithmeticError")

# Дан список. Пользователь не знает его размер. Программа должна бросить исключение TypeError, когда пользователь
# пытается удалить элемент которого нет в списке.
try:
    x = [1, 2, 3, 4, 5]
    x.remove(10)
    raise TypeError
except:
    print("TypeError")

# Дан словарь, который содержит некоторые ключи и значения по этим ключам, пользователь не знает этих ключей. Бросьте
# ошибку KeyError в том случае когда пользователь пытается просмотреть значение по ключу, которого нет в словаре.
try:
    a = {"a": 1, "b": 2, "c": 3}
    print(a["d"])
except KeyError:
    print("KeyError")

# Дана строка, содержащая числа, разделённые пробелами. Нужно вывести их сумму. Если хотя бы один элемент не является
# числом — перехватить исключение и пропустить его. "10 5 abc 3" → 18
a = "1 2 a 4"
lst = a.split(" ")
summ = 0
for i in lst:
    try:
        summ += int(i)
    except ValueError:
        pass
print(summ)

# Написать алгоритм, считающий частоту букв в строке. Если входные данные — не строка, выбросить TypeError.
# Simple input:
# “aaa bb ss rra aa b”
#
# Simple output:
# a 6
# r 2
# b 3
# s 2
# Simple input:
# 42
# Simple output:
# TypeError
try:
    a = "aaa bb ss rra aa b".replace(" ", "")
    unique_letters = set(a)
    for i in unique_letters:
        count = a.count(i)
        print(i, count)
except TypeError:
    print("TypeError")

# Реализовать алгоритм бинарного поиска. Если входной список не отсортирован, выбросить ValueError. Если искомого
# элемента нет, вернуть None
my_list = [1, 3, 5, 6, 7, 8, 9, 10]
def binary_search(lst, item):
    if lst != sorted(lst):
        raise ValueError("Отсортируйте список!")
    minimal = 0
    maximum = len(lst) - 1
    while minimal <= maximum:
        middle = (minimal + maximum) // 2
        if item == lst[middle]:
            return f"Элемент {item} найден под индексом {middle}!"
        elif item < lst[middle]:
            maximum = middle - 1
        else:
            minimal = middle + 1
    return None

print(binary_search(my_list, 7)) # Элемент 7 найден под индексом 4!
print(binary_search(my_list, 6767)) # None
print(binary_search([99, 23, 546, 3, 1, 2], 2)) # ValueError: Отсортируйте список!
