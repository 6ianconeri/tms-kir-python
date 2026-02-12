# Создать текстовый файл и записать в него 6 строк. Записываемые строки вводятся с клавиатуры.
with open("first_task.txt", "w", encoding='utf-8') as file:
    for _ in range(6):
        file.write(str(input("Введите строку: ")) + '\n')

# В конец существующего текстового файла записать три новые строки текста. Записываемые строки вводятся с клавиатуры.
with open("first_task.txt", "a", encoding='utf-8') as file:
    for _ in range(3):
        file.write(str(input("Введите строку: ")) + '\n')

# Дан текстовый файл. Подсчитать количество символов в нем. Без \n
with open("first_task.txt", "r", encoding='utf-8') as file:
    lines = file.readlines()
    summa = 0
    for line in lines:
        line = line.strip('\n')
        summa += len(line)
    print(summa)

# Имеется текстовый файл, содержащий 5 строк. Переписать каждую из его строк в список в том же порядке.
with open('five_strings.txt', 'r', encoding='utf-8') as file:
    lines = [line.strip('\n') for line in file]
    print(lines)

# Имеется текстовый файл. Получить текст, в котором в конце каждой строки из заданного файла добавлен восклицательный знак.
with open('exclamation_mark.txt', 'r', encoding='utf-8') as file:
    lines = [line for line in file if line.strip('\n').endswith('!')]
    print(lines)

# В справочной аэропорта хранится расписание вылета самолетов на следующие сутки. Для каждого рейса указаны номер рейса,
# пункт назначения, время вылета. Вывести все номера рейсов и время вылета самолета для заданного пункта назначения.
# Пример файла flights.json
import json

with open('flights.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    country = input("Введите город: ").lower()

    flights_number = [item["flight_number"] for item in data if item["destination"].lower() == country]
    departures_time = [item["departure_time"] for item in data if item["destination"].lower() == country]

    print(' '.join(flights_number))
    print(' '.join(departures_time))