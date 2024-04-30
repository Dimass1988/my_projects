# 4.1
# number = int(input())
# num_lst = list(str(number))
# a = list(map(int, num_lst))
# sum_left = sum(a[0:3])
# sum_right = sum(a[3:7])
# if sum_right == sum_left:
#     print("ДА")
# else:
#     print("НЕТ")


# t = float(input())
# green = 3
# red = 2
# all_cycle = green + red
# res = t % all_cycle
# if res < green:
#     print("green")
# else:
#     print("red")


# 4.2
# m = int(input())
# if m == 1:
#     print("1. Введение в Python")
# elif m == 2:
#     print("2. Строки и списки")
# elif m == 3:
#     print("3. Условные операторы")
# elif m == 4:
#     print("4. Циклы")
# elif m == 5:
#     print("5. Словари, кортежи и множества")
# elif m == 6:
#     print("6. Выход")
# else:
#     print("Вы выбрали несуществующий пункт меню!")


# a = list(map(int, input().split()))
# a, b, c = a
# if a < b:
#     if a < c:
#         print(a)
#     else:
#         print(c)
# else:
#     if b < c:
#         print(b)
#     else:
#         print(c)


# weight = float(input())
# if 0 < weight <= 60:
#     print(1)
# elif 61 <= weight <= 64:
#     print(2)
# elif 65 <= weight <= 69:
#     print(3)
# else:
#     print(4)


# a = int(input())
# days = {1: 'понедельник', 2: 'вторник', 3: 'среда', 4: 'четверг',
#         5: 'пятница', 6: 'суббота', 7: 'воскресенье'}
# if a in days:
#     print(days.get(a))
# else:
#     print('Вы ввели не верное значение!!!')


# mounths_num = int(input())
# if mounths_num in [1, 3, 5, 7, 8, 10, 12]:
#     print("31")
# elif mounths_num in [4, 6, 9, 11]:
#     print("30")
# else:
#     print("28")


# month, day = map(int, input().split())
# month_previous = 0
# month_next = 0
# day_previous = 0
# day_next = 0
# if 0 < month <= 12:
#     if month == 1:
#         month_previous = 12
#     elif month == 12:
#         month_next = 1
#
#
# print(month_previous, month_next, day)


# days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# b, a = map(int, input().split())
# if a == 1:
#     pday = days[b-2]
#     pmh = b - 1
#     fday = 2
#     fmh = b
# elif a == days[b-1]:
#     pday = a-1
#     pmh = b
#     fday = 1
#     fmh = b+1
# else:
#     pday = a-1
#     pmh = b
#     fday = a+1
#     fmh = b
# print(f"{str(pmh).rjust(2, '0')}.{str(pday).rjust(2, '0')} "
#       f"{str(fmh).rjust(2, '0')}.{str(fday).rjust(2, '0')}")


# day_num = int(input())
# days = {0: 'воскресенье', 1: 'понедельник', 2: 'вторник', 3: 'среда',
#         4: 'четверг', 5: 'пятница', 6: 'суббота', 7: 'воскресенье'}
# z = day_num % 7
# if z in days:
#     print(days.get(z))
# else:
#     print('Вы ввели не верное значение!')

# 4.3


# a = float(input())
# b = float(input())
# d = a if a > b else b
# print(d)


# a = int(input())
# msg = "кратно 3" if a % 3 == 0 else "не кратно 3"
# print(msg)


# word = str(input()).lower()
# word_2 = word[::-1].lower()
# msg = "палиндром" if word == word_2 else "не палиндром"
# print(msg)


num = int(input())
print('False') if num == 0 else print('True')


