# Test 1 Calculator of experience
#
# experience = int(input('Введите число очков опыта: '))
# if experience < 1000:
#     print('Ваш уровень: 1')
# elif 1000 <= experience < 2500:
#     print('Ваш уровень: 2')
# elif 2500 <= experience < 5000:
#     print('Ваш уровень: 3')
# else:
#     print('Ваш уровень: 4')


# Task 2  Max number 2
#
# num_1 = int(input('Введите первое число: '))
# num_2 = int(input('Введите второе число: '))
# num_3 = int(input('Введите третье число: '))
# if num_1 > num_2:
#     if num_3 > num_1:
#         print(num_3)
#     else:
#         print(num_1)
# elif num_2 > num_3:
#     print(num_2)
# else:
#     print(num_3)


# Task 3 Function
#
# x = int(input('Введите число Х: '))
# if x > 0:
#     y = x - 12
# elif x < 0:
#     y = x ** 2
# else:
#     y = 5
# print('y =', y)


# Task 4 Admission
#
# place = int(input('Введите место в списке поступающих: '))
# score = int(input('Введите количество баллов за экзамены: '))
# if place <= 10:
#     print('Поздравляем, Вы поступили!')
#     if score >= 290:
#         print('Бонусом Вам будет начисляться стипендия')
#     else:
#         print('Но Вам не хватило баллов для стипендии')
# else:
#     print('Вы не поступили!')
#

# Task 5 Restaurant
#
# day = int(input('Введите номер дня недели (1 до 7): '))
# hours = int(input('Введите количество часов до конца рабочего дня (0 до 8): '))
# if hours < 1 or hours > 8:
#     print('Некорректное количество часов')
#
# if day < 1 or day > 7:
#     print('Некорректный номер дня недели')
# elif day == 1:
#     print('Сегодня понедельник.')
# elif day == 2:
#     print('Сегодня вторник')
# elif day == 3:
#     print('Сегодня среда')
# elif day == 4:
#     print('Сегодня четверг')
# elif day == 7:
#     print('Сегодня воскресенье')
# elif day == 6:
#     print('Сегодня суббота')
# else:
#     print('Сегодня пятница')
#     if hours < 2:
#         print('Можно уйти пораньше!')
# print('Осталось работать', hours, 'часа')
#

# Task 6 Free cash register
#
# clients = int(input('Количество клиентов: '))
# seller = int(input('Количество продавцов: '))
# salary = int(input('Зарплата одного продавца: '))
# if clients / seller > 4:
#     print('Слишком мало продавцов!')
#     if salary < 20000:
#         salary += 2000
#         print('Зарплата повышена до', salary, 'рублей')
# else:
#     print('Продавцов достаточно')
# print('Зарплата одного продавца составляет', salary, 'рублей')


# Task 7 Protection from fool
#
# number = int(input('Введите число: '))
# if 9 < number < 100:
#     print('Число двузначное')
# else:
#     print('Число не двузначное')


# Task 8 School break
#
# number_1 = int(input('Загадайте первое число: '))
# number_2 = int(input('Загадайте второе число: '))
# if number_1 % 2 == 0 or number_2 % 2 == 0:
#     print('Одно из чисел чётное. Учитель заслужил конфету!')
# elif number_1 % 2 != 0 and number_2 % 2 != 0:
#     print('Учитель отдает конфету')


