
# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

n = str(input('Введите число, сумму цифр которого хотите посчитать: '))
print(n)

numb = n.replace('.', '')
print(numb)
rez = 0
for i in range(len(numb)):
    rez = rez+int(numb[i])
print(rez)


# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
number = int(input('Введите число, сумму цифр которого хотите посчитать: '))

def proiz(n):
    pr = 1
    for i in range(1, n+1):
        pr = pr*i
        print(pr, end=' ')

proiz(number)

# 3. Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

number = int(input('Введите число, сумму цифр которого хотите посчитать: '))

def sumNumber(n):
    s = 1
    for i in range(1, n+1):
        s = s+3
        print(s, end=' ')

sumNumber(number)

# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
#  Найдите произведение элементов на указанных позициях.
#  Позиции задаются пользователем с клавиатуры.


import random

N = int(input('Введите позицию N: '))

listNumbers = [random.randint(-10, 10) for i in range(10)]
pozition1 = int(input('Введите позицию первого множителя: '))
pozition2 = int(input('Введите позицию второго множителя: '))

print(listNumbers)

def find_proiz(n1=1, n2=1):
   
    for i in range(len(listNumbers)):
        if n1 == i:
            n1 = listNumbers[i]
            print(f"{n1}")
        if n2 == i:
            n2 = listNumbers[i]

            print(f'{n2}')
    print(n2*n1)

find_proiz(pozition1, pozition2)


# 5. Реализуйте алгоритм перемешивания списка.

someList = [random.randint(-20, 30) for i in range(10)]
print(someList)

someList.sort()
print(someList)
