# Дан кортеж. Найти разность между его максимальным и минимальный элементом
my_tuple = (1, 5, 9, 10, 123, 2)
minimum = min(my_tuple)
maximum = max(my_tuple)
print(maximum - minimum)

# Дан кортеж. Написать программу, определяющую сколько раз менялся знак в кортеже. (5,2,-2,7,-8,-9,1) 4 раза
my_tuple = (5, 2, -2, 7, -8, -9, 1)
count = 0
for index in range(len(my_tuple) - 1):
    if my_tuple[index] * my_tuple[index + 1] < 0:
        count += 1
print(count)

# Дан кортеж. Вывести на экран все простые числа в данном кортеже.
my_tuple = (1, 2, 3, 5, 6, 19, 7)
new_tuple = tuple()
for elem in my_tuple:
    if elem > 1:
        is_prime = True
        for i in range(2, int(elem**0.5) + 1):
            if elem % i == 0:
                is_prime = False
                break
        if is_prime:
            print(elem)

# *Дан кортеж. Без функций и дополнительных списков вывести все повторяющиеся элементы. (count не использовать). (1,2,4,1,2,6) 1 2
my_tuple = (1, 2, 4, 1, 2, 6)
for index in range(len(my_tuple) - 1):
    if my_tuple[index] == my_tuple[index + 1]:
        print(my_tuple[index])
        index += 1

# СПИСКИ
# Задано два списка. Найти наименьшие среди элементов первого списка, которые не входят во второй список.
# [4,1,6,9] [8,1,2,4,9,5,7,6] -> нет такого элемента
dict_1 = [4, 1, 6, 9, 3, -10]
dict_2 = [8, 1, 2, 4, 9, 5, 7, 6]
dict_3 = []
for elem in dict_1:
    if elem not in dict_2:
        dict_3.append(elem)
print(min(dict_3))

# Дан список положительных целых чисел. Вставить после каждого чётного числа его перевёртыш. 18 81, 42 24, 8 8, 122 221
var_dict = [18, 19, 24, 13, 8, 122]
result = []
for elem in var_dict:
    result.append(elem)
    if elem % 2 == 0:
        result.append(int(str(elem)[::-1]))
print(result)

# Дан список. Вычислить сколько раз в нем встречается каждый элемент, не используя сортировки. [5,2,4,5,1,2] 1 – 1 2 – 2 4 – 1 5 - 2
var_dict = [5, 2, 4, 5, 1, 2]
var_set = set(var_dict)
for elem in var_set:
    print(f"{elem} - {var_dict.count(elem)}")

# *Дан список. Перезаписать его так, чтобы сначала были все положительные числа, а затем все отрицательные и нули,
# сохраняя порядок их следования. [5,2,0,-2,-7,1,8,0,-1] -> [5,2,1,8,-2,-7,-1,0,0]

lst = [5,2,0,-2,-7,1,8,0,-1]
list_result = []
list_min = []
list_zero = []

for item in lst:
    if item > 0:
        list_result.append(item)
    if item < 0:
        list_min.append(item)
    if item == 0:
        list_zero.append(item)
list_result = list_result + list_min + list_zero
print(list_result)

# *Дан список. Продублировать все неповторяющиеся элементы.
# [5,2,7,3,8,2,4,1,6,5] -> [5,2,7,7,3,3,8,8,2,4,4,1,1,6,6,5]

lst = [5, 2, 7, 3, 8, 2, 4, 1, 6, 5]
result = []

for i in range(len(lst)):
    result.append(lst[i])
    if lst.count(lst[i]) == 1:
        result.append(lst[i])

print(result)

# МНОЖЕСТВА
# Во входной строке записана последовательность чисел через пробел. Для каждого числа выведите слово YES (в отдельной
# строке), если это число ранее встречалось в последовательности или NO, если не встречалось.
numbers = "1 1 1 2 3 2 1 4 12 2 1 2 4 6".split()
new_set = set()
for i in numbers:
    if i in new_set:
        print("YES")
    else:
        print("NO")
        new_set.add(i)

# СЛОВАРИ
# Создайте словарь, связав его с переменной school, и наполните данными, которые бы отражали количество учащихся в
# разных 9 классах (9а, 9б, 9в, 9м, 9ф и т.п.). Внесите изменения в словарь согласно следующему:
# а) в одном из классов изменилось количество учащихся
# б) в школе появился новый класс.
# в) в школе был расформирован (удален) другой класс.
# г) Вычислите общее количество учащихся 9 классов в школе.
school = {
    "9a": 20,
    "9b": 15,
    "9v": 15,
    "9g": 33
}

school["9a"] = 25
print(school)

school["9c"] = 15
print(school)

del school["9b"]
print(school)

result = 0
for values in school.values():
    result += values
print(result)

# Словари вторая задача:
my_dict = {}
while True:
    key = input("Введите термин: ")
    if key == ".":
        break
    value = input("Введите значение: ")
    my_dict[key] = value
counter = int(input("Введите кол-во терминов: "))
for _ in range(counter):
    my_key = input("Введите термин для поиска: ")
    if my_key in my_dict:
        print(f"Значение {my_dict[my_key]}")
    else:
        print("Не найдено!")

