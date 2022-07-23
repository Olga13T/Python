# list список - изменяемый, индексируемый
# tuple() - не изменяемый, индексируемый
# set() - изменяемый, не индексируемый
# dict() - изменяемый, не индексируемый

# my_set={1,12,7,4}
# for item in my_set:
#     print(item)
# print(my_set)

# dict
# my_dict = {
#     12: 'table',
#     54: 'bed'
# }

# 1. Задайте список. Напишите программу, которая определит,
# присутствует ли в заданном списке строк некое число.

# '12' -> ['asd12', '12', 'asd', '87'] -> 'asd12', '12'
# my_list = ['asd12', '12', 'asd', '87']
# for i in my_list:
#     if 'asd' in i:
#         print(i)


# 2. Напишите программу, которая определит позицию второго
# вхождения строки в списке либо сообщит, что её нет.
# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1

# count = 0
# my_list = [ "фыв", "ячс", "цук", "йцукен"]
# for i in range(len(my_list)):
#     if my_list[i] == 'йцу':
#         count += 1
#         if count<1:
#             print('-1')

#         if count > 1:
#             print(i)
#             break

# Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.

import time

# a = str(time.time())
# b=a[-1]+a[-2]

# print(b)


someList = [(((time.time())%100)/3) for i in range(7)]
print(someList)

# def find_num(x):
#     a = str(time.time())
#     b = ''
#     count = 1
#     while count <= x:
#         b += a[-count]
#         count += 1
#     return int(b)

# print(find_num(2))

# import time

# l = int(input('Введите длинну числа: '))

# ms = int(((time.time() % 1) * (10 ** (l + 1))) % (10 ** (l)))
# #ms = time.time()
# #ms = int(time.time() % 10)

# print(ms)

# my_set = set()
# for i in range(100):
#     my_set.add(str(i))

# for e in my_set:
#     print(int(e))

# import time

# l = int(input('Введите длинну числа: '))

# ms = int(((time.time() % 1) * (10 ** (l + 1))) % (10 ** (l)))
# #ms = time.time()
# #ms = int(time.time() % 10)

# print(ms)

# from datetime import datetime 
# num = datetime.now()
# print(num.microsecond//1000)

# import time
# b = int(time.time())
# count = b%100
# if count == 0:
#     print (0)
# else:    
#     print(b%count*count)

# # супер вариант

# import time

# def sum_numbers(number):
#     sum = 0
#     for i in range(len(number)):
#         if number[i].isdigit():
#             sum += int(number[i])
#     return sum


# seconds = str(time.time())
# print(seconds)
# print(sum_numbers(seconds))

# import time

# def find_num(x):
#     a = str(time.time())
#     b = ''
#     count = 1
#     while count <= x:
#         if a[-count] == '.':
#             continue
#         b += a[-count]
#         count += 1
#     return int(b)


# print(find_num(3))

# import time

# l = int(input('Введите длинну числа: '))
# a = time.time()
# print(a)
# ms = int(((a % 1) * (10 ** (l + 1))) % (10 ** (l)))
# #ms = time.time()
# #ms = int(time.time() % 10)

# print(ms)


