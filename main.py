# Задание к модулю 18
# Выполнила Догадина Анастасия группа 108

print("********************************************")
print("************* ПРОДАЖА БИЛЕТОВ! *************")
print("********************************************")

# Переменная добавленная для проверки корректности введенных данных, пока False не дает программе идти дальше
is_right = False
count_of_tickets = 0  # Кол-во билетов
while not is_right:
    try:
        count_of_tickets = int(input("Введите необходимое кол-во билетов: "))
        if count_of_tickets <= 0:
            raise ValueError()
        is_right = True
    except ValueError:
        print("Введите корректное значение")

cost = 0  # Общая стоимость

for person in range(count_of_tickets):
    is_right = False
    age = 0  # Возраст человека
    while not is_right:
        try:
            age = int(input(f'Введите возраст посетителя номер {person + 1}: '))
            if age < 0:
                raise ValueError()
            if age > 100:
                print('\nМы вам поверим, но мы вам не верим -_- \n')
            is_right = True
        except ValueError:
            print("Введите корректное значение (положительное число)")

    if age >= 25:
        cost += 1390
    elif 18 <= age < 25:
        cost += 990
    else:
        continue

if count_of_tickets > 2:
    cost *= 0.9
print("\nРезультат:")
print(f"Общая стоимость билетов{' (с учетом скидки)' if count_of_tickets > 2 else ''}:", cost, "рублей")
print("Хорошего дня!")
