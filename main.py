# Задание к модулю 18
# Выполнила Догадина Анастасия группа 108

print("********************************************")
print("************* ПРОДАЖА БИЛЕТОВ! *************")
print("********************************************")

is_right = False # Переменная добавленная для проверки корректности введенных данных, пока False не дает программе идти дальше
count_of_tickets = 0 # Кол-во билетов
while not is_right:
    try:
        count_of_tickets = int(input("Введите необходимое кол-во билетов: "))
        if count_of_tickets <= 0:
            raise ValueError()
        is_right = True
    except ValueError:
        print("Введите корректное значение")
cost = 0

for person in range(count_of_tickets):
    is_right = False
    age = 0 # Возраст человека
    while not is_right:
        try:
            age = int(input('Введите возраст посетителя номер {} '.format(person + 1)))
            if age < 0:
                raise ValueError()
            is_right = True
        except ValueError:
            print("Введите корректное значение")

    if age >= 25:
        cost = cost + 1390
    elif 18 <= age < 25:
        cost = cost + 990
    else:
        continue

if count_of_tickets > 2:
    cost = cost * 0.9

print("Общая стоимость билетов:", cost, "рублей")
print("Хорошего дня!")