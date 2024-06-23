# Task 1 Weather sensor
#
# weather = int(input('На улице идет дождь? (1/0)'))
# if weather == 1:
#     print('Пошёл дождь. Возьмите зонтик!')
# else:
#     print('Дождя нет.')


# Task 2 Admission
#
# points_rus = int(input('Введите кол-во баллов по русскому языку: '))
# points_math = int(input('Введите кол-во баллов по математике: '))
# points_inform = int(input('Введите кол-во баллов по информатике: '))
# if points_rus + points_math + points_inform >= 270:
#     print('Поздравляю, ты поступил на бюджет!')
# else:
#     print('К сожалению, ты не прошел на бюджет.')


# Task 3 Take care of the teeth
#
# num = int(input('Введите число: '))
# if num % 2 == 1:
#     print('Нечетное число.')
# else:
#     print('Четное число')


# Task 4 Discount calculator
#
# product_1 = int(input('Введите стоимость первого товара: '))
# product_2 = int(input('Введите стоимость второго товара: '))
# product_3 = int(input('Введите стоимость третьего товара: '))
# sum = product_1 + product_2 + product_3
# if sum >= 10000:
#     price = sum / 100 * 10
#     sum -= price
#     print('Сумма товаров: ', sum)


# Task 5 The absolut value of a number
#
# num = int(input('Введите число: '))
# if num < 0:
#     answer = -num
# else:
#     answer = num
# print('Ввели', num, 'ответ', answer)


# Task 6 Dice game
#
# cube_Kostya = int(input('Кубик Кости: '))
# cube_master = int(input('Кубик владельца: '))
# if cube_Kostya >= cube_master:
#     print('Разность чисел: ', cube_Kostya - cube_master)
#     print('Костя платит.')
# else:
#     print('Сумма:', cube_Kostya + cube_master)
#     print('Владелец платит.')
# print('Игра окончена')


# Task 7 ATM
#
# sum = int(input('Введите сумму, которую хотите снять: '))
# if sum % 100 != 0:
#     print('Такую сумму снять невозможно. Обратитесь в другой банкомат.')
# else:
#     print('Заберите деньги из купюроприемника')


# Task 8 Difficult life
#
# hours = int(input('Введите отработанные часы: '))
# credit = int(input('Введите остаток по кредиту: '))
# food = int(input('Введите траты на еду: '))
# salary = (200 * hours) / 2**3 + hours
# if salary >= credit + food:
#     print('Часов хватает. Можно отдохнуть.')
# else:
#     print('Часов не хватает. Придется работать!')


# Task 9 Bad dial
#
# mileage = int(input('Введите пробег (трехзначное число): '))
# day = int(input('Введите номер дня: '))
# summ = (mileage // 100) + (mileage // 10 % 10) + (mileage % 10)
# if summ > day:
#     print('Сброс, пробег обнулен')
#     mileage = 0
# else:
#     print("Сегодня не сломался")
# print('Текущий пробег:', mileage)