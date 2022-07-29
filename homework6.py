# Задача: предложить улучшения кода для уже решённых задач. ПЯТЬ ШТУК:
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension
# В этом случае можно пропустить совсем тривиальные
# (т.е. задачу 1 или 2 тут точно решать не имеет смысла) - исходите из уровня группы и студента.

# 4.  Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
# decimalNumber = int(input('десятичное число:  '))
# binarNumber = ''
# while decimalNumber > 0:
#     binarNumber = str(decimalNumber % 2)+binarNumber
#     decimalNumber //= 2
# print(binarNumber)

# 6. Задайте два числа. Напишите программу,
#  которая найдёт НОК (наименьшее общее кратное)
#  этих двух чисел.

# num1 = 35
# num2 = 14
# while num2 > 0:
#     num1, num2 = num2, num1 % num2
# print(num1)


# 3. Задайте список из вещественных чисел. Напишите программу,
#  которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
# n_max = 0
# n_min = 1000

# some = [1.1, 1.2, 3.1, 5, 10.01]

#  res = [word for word in my_str.split() if 'абв' not in word]
# list(filter([item for item in (my_list) if my_list.count==1]))
# result_some = [i for i in ((some*100) % 100)]
# print(max(result_some) - min(result_some))
# for i in range(len(list)):
#     list[i] = list[i]*100
#     list[i] = list[i] % 100
#     for i in range(len(list)):
#         if list[i] > n_max:
#             n_max = list[i]
#         elif list[i] < n_min and list[i]>0:
#             n_min = list[i]

# print(list)
# print('max =  {n_max}')
# print('min = {n_min}')
# print('разница между max и min значением :')
# print((n_max-n_min)/100)

# 1. Задайте список из нескольких чисел.
#  Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

#    0  1  2  3  4  5  6
# s=[2, 3, 5, 3, 6, 4, 8]

# res=[item for item in s if not (s.index(item) % 2 == 0)]
# print(res)

# Было:
# s = input('enter list:  ').split()
# notEven = []
# for i in range(len(s)):
#     s[i] = int(s[i])
#     if not i % 2:
#         notEven.append(s[i])
# print(sum(notEven))


# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
# number = int(input('Введите число, сумму цифр которого хотите посчитать: '))
# def proiz(n):
#     pr = 1
#     for i in range(1, n+1):
#         pr = pr*i
#         print(pr, end=' ')
# proiz(number)

from math import factorial


numberN = 4
f = factorial(numberN)
# print(factorial(numberN))

itogos = [i for i in range(1,f)]
print(itogos)