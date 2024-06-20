# Task 1 Language of mathematics
#
# a, b, c, d = 8, 10, 12, 18
# res = ((-3 + a ** 2) * b - 2 ** 3) / (c - 2 * d)
# print(res)


# Task 2 Joker
#
# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))
# a *= 3
# b %= 8
# print(a + b)


# Task 3 Financial report
#
# a = int(input('Число первое: '))
# b = int(input('Число второе: '))
# c = int(input('Число третье: '))
# d = int(input('Число четвертое: '))
# print((a + b) / (c + d))


# Task 4 Next and previous
#
# a = int(input('Введите число: '))
# print('После числа ', a, 'идёт число ', a + 1)
# print('До числа ', a, 'идёт число ', a - 1)


# Task 5 Bike
#
# print('Решите пример: 50 * 2 ** 3 - 32')
# user_answer = int(input('Ваш ответ: '))
# correct_answer = 50 * 2 ** 3 - 32
# print('Верный ответ:', correct_answer)
# print('Ваш ответ:', user_answer)


# Task 6 Area of a triangle
#
# a = int(input('Введите длину катета: '))
# b = int(input('Введите другую длину катета: '))
# print((a * b) / 2)

# Task 7 Clock
#
# minutes = int(input('Введите n — количество минут: '))
# time = minutes // 60
# remainder_time = minutes % 60
# print(time, remainder_time)


# Task 8
#
# first_number = int(input('Введите первое число: '))
# second_number = int(input('Введите второе число: '))
# sum = (first_number % 100) + (second_number % 100)
# print(sum)


# Task 9 A round trip
#
# road = 115
# speed = int(input('Введите скорость в км/ч: '))
# time = float(input('Введите время через какое он оставится в часах: '))
# print('Пройденное расстояние составит', speed * time,
#       'км и он будет на отметке', (speed * time) % road,
#       'км и пройдет', ((speed * time) // road), 'круга(ов)')


# Task 10 Pie
#
# a = int(input('Пирожок в столовой стоит столько-то рублей: '))
# b = int(input('и столько-то копеек: '))
# n = int(input('Введите количество пирожков: '))
# print('Стоимость покупки составит: ', n * (a + b / 100),
#       'в рублях, а в копейках составит: ', (n * (a + b / 100)) * 100)


# Task 11 Сut the number into pieces
#
# num = int(input('Введите четырехзначное число: '))
# a = num // 1000
# b = num // 100 % 10
# c = (num % 100) // 10
# d = num % 10
# print(a, b, c, d)


# Task 12 In reverse order
#
# num = int(input('Введите четырехзначное число: '))
# a = num // 1000
# b = num // 100 % 10
# c = (num % 100) // 10
# d = num % 10
# print(d, c, b, a)


# Task 13 Swap
#
# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))
# print(a,b)
# a += b
# b = a - b
# a -= b
# print(a,b)
