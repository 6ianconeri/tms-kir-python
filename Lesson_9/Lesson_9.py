# Напишите функцию m(a, b), вычисляющую минимум двух чисел. С помощью вашей функции найдите минимальное четырёх чисел.
def m(a, b):
    minimum = a
    if a > b:
        minimum = b
    return minimum

print(m(m(10, 5), m(30, 15)))

# Дано натуральное число n > 1. Проверьте, является ли оно совершенным. Программа должна вывести слово YES,
# если число совершенное и NO, в противном случае.
def perfect_num(a):
    summ = 0
    for i in range(1, a):
        if a % i == 0:
            summ += i
            if summ == a:
                return "YES"
    return "NO"

print(perfect_num(496))

# Напишите функцию fib(n), которая по данному целому неотрицательному n возвращает n-e число Фибоначчи. Ищем число
# Фиббоначи через цикл! Рекурсию не использовать!
def fib(n):
    if n <= 1:
        return n
    previous = 0
    current = 1
    for _ in range(2, n + 1):
        previous, current = current, previous + current

    return current

print(fib(8))

# В языке Python есть некоторые ограничения на имена переменных. Имена переменных
# - могут состоять только из цифр, букв и знаков подчеркивания.
# -не могут начинаться с цифры.
# Программист вводит строки с именами переменных. Для каждой переменной нужно вывести "Можно использовать", если ее имя
# корректно, или "Нельзя использовать", если это не так. Определив все нужные переменные, программист заканчивает ввод
# строкой "Поработали, и хватит".
# Для проверки каждой строки используйте функцию check_variable(v). Для простоты будем считать, что программист использует
# только латинские буквы.  Не может содержать: ! @ # $ % ^ & * ()
def check_var(some_str):
    bad_char_list = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]
    if some_str[0].isdigit():
        return "Нельзя использовать"

    for char in some_str:
        if char in bad_char_list:
            return "Нельзя использовать"
    return "Можно использовать"

while True:
    user_str = input("Введите переменную: ")

    if user_str == "Поработали, и хватит":
        break

    result = check_var(user_str)
    print(result)

# Сгенерировать список нечётных двузначных чисел.
lst = [i for i in range(10, 100) if i % 2 != 0]
print(lst)

# Сгенерировать список всех трёхзначных чисел кратных 5 и 3.
lst = [i for i in range(100, 1000) if i % 5 == 0 and i % 3 == 0]
print(lst)


# Дан список, упорядоченный по не убыванию элементов в нем. Напишите функцию которая определяет количество в нем
# различных элементов. set функцию не использовать.
some_lst = [1, 2, 3, 3, 3, 4, 5, 66, 66, 77, 99, 100, 100]
def unique_elem_fun(lst):
    counter = 0
    for item in lst:
        if lst.count(item) == 1:
            counter += 1
    return counter

print(unique_elem_fun(some_lst))

# Напишите программу, на вход которой подаётся список чисел одной строкой. Программа должна для каждого элемента этого
# списка вывести сумму двух его соседей. Для элементов списка, являющихся крайними, одним из соседей считается элемент,
# находящий на противоположном конце этого списка. Например, если на вход подаётся список "1 3 5 6 10", то на выход
# ожидается список "13 6 9 15 7" (без кавычек).Если на вход пришло только одно число, надо вывести его же. Вывод должен
# содержать одну строку с числами нового списка, разделёнными пробелом.
#
# Sample Input 1:
# 1 3 5 6 10
# Sample Output 1:
# 13 6 9 15 7
# Sample Input 2:
# 10
# Sample Output 2:
# 10
# Sample Input 3:
# 10 2
# Sample Output 3:
# 4 20
string_1 = "1 3 5 6 10"
def sum_neighbours_fun(string):
    lst = string.split(" ")
    new_lst = []
    for index in range(len(lst)):
        if len(lst) == 1:
            new_lst.append(lst[index])
            break
        if index == len(lst) - 1:
            new_lst.append(int(lst[index - 1]) + int(lst[0]))
        else:
            new_lst.append(int(lst[index - 1]) + int(lst[index + 1]))
    return " ".join(map(str, new_lst))

print(sum_neighbours_fun(string_1))

# Дан список, состоящий из строк. Отсортировать его по длине слов. Сначала должны идти длинные слова затем короткие.
lst = ["a", "aaaa", "aa", "aaaaaaaaa", "aaa", "a"]
lst.sort(reverse=True)
print(lst)

# Дан список состоящий из слов. Отсортировать его по количеству вхождений буквы 'a'
lst = ["kaaas", "kaa", "kaaaaaaa", "kaaaa", "kabbbbbbbbbbbbbbbbbbbbbbb"]
new_lst = sorted(lst, key = lambda x: x.count("a"))
print(new_lst)

