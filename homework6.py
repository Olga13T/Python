# Задача: предложить улучшения кода для уже решённых задач. ПЯТЬ ШТУК:
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension
# В этом случае можно пропустить совсем тривиальные
# (т.е. задачу 1 или 2 тут точно решать не имеет смысла) - исходите из уровня группы и студента.

# 1. Задайте список из вещественных чисел. Напишите программу,
#  которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
# n_max = 0
# n_min = 1000

my_list = [1.1, 1.2, 3.1, 5.1, 10.01]

res = [((item*100) % 100)/100 for item in my_list]
print(max(res)-min(res))
# было:
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


# 2. Задайте список из нескольких чисел.
#  Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

#    0  1  2  3  4  5  6
s=[2, 3, 5, 3, 6, 4, 8]

res=[item for item in s if not (s.index(item) % 2 == 0)]
print(res)

# Было:
# s = input('enter list:  ').split()
# notEven = []
# for i in range(len(s)):
#     s[i] = int(s[i])
#     if not i % 2:
#         notEven.append(s[i])
# print(sum(notEven))

# 3. Задайте два числа. Напишите программу,
#  которая найдёт НОК (наименьшее общее кратное)
#  этих двух чисел.

n1= map(int, input('Введите 1e число _').split())
n2 = map(int, input('Введите 2e число _').split())

def min_devis(num1, num2):
    while num2 % num1 != 0:
        num1, num2 = num2, num1 % num2
    print(num1)

min_devis(n1, n2)

# 3. Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.

file_path = r'homework4_file.txt'

with open(file_path, 'r') as f:
    mystr = f.read()

file_new = [i for i in mystr.split() if mystr.count(i)==1]
print(file_new)

# было:
# mystr = mystr.split()
# for i in range(len(mystr)):
#     mystr[i] = int(mystr[i])

# for i in mystr:
#     if mystr.count(i)==1:
#         unic_str.append(i)  
# print(mystr)
# print(unic_str)

# 4. Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

a = int(input('Введите цифру, обозначающую день недели (от 1 до 7):  '))

c = lambda x: 'no' if 0 < x < 6 else ('yes' if 5 < x < 8 else 'Введенное число не соответствует дню недели')
print(c(a))
# vscod - сам переделал при авто-форматировании с лямбдой на def?! - это что-то вроде оптимизации?
# Тоже рабочий вариант, но короче..
# def cho(x): return 'no' if 0 < x < 6 else ('yes' if 5 < x < 8 else 'Введенное число не соответствует дню недели')

# 5. Реализуйте алгоритм перемешивания списка.

import random

someList = [random.randint(-20, 30) for i in range(10)]
print(someList)

s_even = [i for i in someList if i % 2 == 0]
n_even = [i for i in someList if i % 2 != 0]

print(s_even+n_even)

# было:
# someList.sort()
# print(someList)
