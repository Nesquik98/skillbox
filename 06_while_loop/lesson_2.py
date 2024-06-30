# Task 1 Running is useful
#
# weather = int(input('Введите температуру: '))
# run = 0
# while weather > 15:
#     run += 20
#     weather -= 2
#     if weather <= 15:
#         print('Пройдено метров:', run)
#         break
#     run += 10
#     print('Пройдено метров:', run)


# Task 2 Decoding the code*
#
# numbers = int(input('Введите большое число: '))
# summ = 0
# while numbers > 0:
#     lust_num = numbers % 10
#     if lust_num == 5:
#         print('Разрыв')
#         break
#     summ += lust_num
#     numbers //= 10
# print(summ)


# Task 3 Primary school
#
# count = 0
# numbers = 0
# while numbers >= 0:
#     numbers = int(input('Введите число: '))
#     count += 1
# print('Количество введенных чисел:', count)


# Task 4 Bets accepted, no more bets

# total_money = int(input('Введите стартовую сумму: '))
# while total_money < 10000:
#     cub_num = int(input('Сколько выпало на кубике? '))
#     if cub_num == 3:
#         print('Вы проиграли всё!')
#         total_money = 0
#         print('Игра закончена.')
#         break
#     else:
#         print('Выиграли 500 рублей!')
#         total_money += 500
# print('Итого осталось:', total_money)