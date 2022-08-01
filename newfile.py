# 1. Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# # - 1 -> нет

# a = int(input('Введите цифру, обозначающую день недели (от 1 до 7):  '))


# # def cho(x): return 'no' if 0 < x < 6 else ('yes' if 5 < x < 8 else 'Введенное число не соответствует дню недели')

# c = lambda x: 'no' if 0 < x < 6 else ('yes' if 5 < x < 8 else 'Введенное число не соответствует дню недели')
# print(c(a))
# check_day = print(dict.get(lambda d, : a))
# def choice(x):
#     if 0 < x < 6:
#         return 'нет'
#     elif 5 < x < 8:
#         return 'да'
#     else:
#         return ''
# print(choice(a))
import random

someList = [random.randint(-20, 30) for i in range(10)]
print(someList)

s_even = [i for i in someList if i % 2 == 0]
n_even = [i for i in someList if i % 2 != 0]

print(s_even+n_even)