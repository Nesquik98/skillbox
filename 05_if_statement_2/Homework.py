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


# Task 9 Deuce again
#
# rating = int(input('Что получил по математике? '))
# if 2 <= rating <= 3:
#  print('Плохо. Марш учиться!')
# elif 4 <= rating <= 5:
#  print('Молодец! Можешь отдохнуть.')


# Task 10 Protection from fool 2
#
# number = int(input('Введите число: '))
# if 9 < number < 100 or -100 < number < 9:
#     print('Число двузначное')
# else:
#     print('Число не двузначное')


# Task 11 Kostya wants to win
#
# num_1 = int(input('Первое число: '))
# num_2 = int(input('Второе число: '))
# num_3 = int(input('Третье число: '))
# if num_1 == num_2 and num_1 == num_3:
#     print('3')
# elif num_1 == num_2 or num_1 == num_3 or num_2 == num_3:
#     print('2')
# else:
#     print('0')


# Task 12 Lazy business
#
# num_1 = int(input('Количество станков (шт): '))
# num_2 = int(input('Площадь помещения (м2): '))
# if num_2 >= 100 and num_2 >= 5:
#     print('Всё отлично, это наш вариант!')
# else:
#     print('Не подходит. Нужно искать дальше')


# Task 13 Housewarming
#
# price = int(input('Стоимость квартиры (млн): '))
# s = int(input('Площадь квартиры (м2): '))
# if s >= 100 and price <= 10:
#     print('Подходит')
# elif (80 <= s < 100) and price <= 7:
#     print('Подходит')
# else:
#     print('Не подходит')


# Task 14 Progressive tax 2
#
# wallet = int(input('Введите свою прибыль: '))
# if wallet <= 10000:
#     wallet *= 13 / 100
#     print('Размер налога (13%) равен:', wallet)
# elif 10000 <= wallet < 50000:
#     tax = ((wallet - 10000) * 20 / 100) + 10000 * 13 / 100
#     print('Размер налога (20%) равен:', tax)
# elif wallet >= 50000:
#     tax = ((wallet - 50000) * 30 / 100) + ((50000 - 10000) * 20 / 100) + (10000 * 13 / 100)
#     print('Размер налога (30%) равен:', tax)


# Task 15 Mail
#
# time = int(input('Введите время на часах (от 0 до 23): '))
# if (8 <= time < 10) or (12 <= time < 14) or (16 <= time < 18) or (20 <= time < 22):
#     print('Можно получить посылку')
# else:
#     print('Посылку получить нельзя')