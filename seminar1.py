# написать программу,которая принимает на вход 2 числа
# и отвечает является квадратом илли нет
# 5,25 - да
# 25, 5 - да
# 1,16 - нет

# a = int(input('Введите число а = '))
# b = int(input('Введите число b = '))
# if a == b*b:
#     print(f'{a}', '{b}' - "да")
# elif b == a*a:
#     print(f'{a}', '{b}' - "да")
# else:
#     print(f'{a}', '{b}' - "нет")

# тернарные операторы
# a = int(input('Введите число а = '))
# b = int(input('Введите число b = '))

# print('yes' if ((a == b*b) or (b == a*a)) else 'no') ##вложенность


# a = int(input('Введите число а = '))
# b = int(input('Введите число b = '))
# if (a == b*b) or (b == a*a):
#     print(f"да")
# else:
#     print(f"нет")


# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

#     Примеры:

#     - 1, 4, 8, 7, 5 -> 8
#     - 78, 55, 36, 90, 2 -> 90

# list = [1,2,3,4,5]
# a = max
# for i in list:
#     if i > max:
#         max = i
# print(i)

# list = [1,11,56,2,8]
# print(f'Максимальное число: {max(list)}')
# z=0
# while z<6:
#     a=list(input('Введите число: '))
#     z+=1
# i=1
# max=a[0]
# while (i!=len(a)):
#     if(a[i]>max):
#         max=a[i]
#         i+=1
#     else:
#         i+=1
# print(max)

# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

#     Примеры:

#     - 1, 4, 8, 7, 5 -> 8
#     - 78, 55, 36, 90, 2 -> 90

# maxx = 0
# for i in range(5):
#     x = int(input('--> '))
#     if i == 0:
#         maxx = x
#     elif x > maxx:
#         maxx = x

# print(maxx)


# Добавление в список
# my_list = []

# for i in range(5):
#     x = int(input('--> '))
#     my_list.append(x)

# Удаление
# my_list = [5, 2, 6]

# my_list.pop(1)
# print(my_list)
# my_list.remove(6)
# print(my_list)

# my_list = [6, 5, 2, 6]

# while 6 in my_list:
#     my_list.remove(6)

# print(my_list)

# программу, которая на вход принимает 5 чисел и находит максимальное из них.

#     Примеры:
#     - 78, 55, 36, 90, 2 -> 90
# from ast import While


# While

# my_list = [5, 2, 9, 1, 3]
# i = 1
# maxx = my_list[0]
# while i < len(my_list):
#     if my_list[i] > maxx:
#         maxx = my_list[i]
#     i += 1

# print(maxx)

# 1. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

#     *Примеры:*

#     - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

# n = int(input('Введите число N -> '))
# for i in range(-n, n + 1):
#     print(i, end=' ')

# n = int(input('Введите число x = '))
# a = -n
# while a < n + 1:
#     print(a, end = ' ')
#     a += 1


# 2. Напишите программу, которая будет принимать на вход дробь и показывать
# первую цифру дробной части числа.
#     - 6,78 -> 7
#     - 5 -> нет
#     - 0,34 -> 3

# x=float(input('-> '))
# x*=10
# x=int(x)
# print(x%10)

# 3. Напишите программу, которая принимает на вход число и проверяет,
# кратно ли оно (5 и 10) или (15, но не 30).
# x=int(input('-> '))
# if((x%5==0 and x%10==0) or (x%15==0 and x%30!=30)):
#     print('yes')

# str = '978'
# for i in range(len(str)):
#     if str[i]==',':
#         print(str[i+1], end=' ')

# ¬ - not
# ⋁ - or
# ⋀ - and

# rezult = True
# for X in True, False:
#     for Y in True, False:
#         for Z in True, False:
#             rezult = rezult and (not(X or Y or Z) == (not X and not Y and not Z))
#             print(rezult)



# rezult = True
# for x in True, False:
#     for y in True, False:
#         for z in True, False:
#             print(f"{x= } {y= } {z= }   result:{not(x or y or z) == (not x and not y and not z)}")
