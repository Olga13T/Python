# 1. Задайте список из нескольких чисел.
#  Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

s = input('enter list:  ').split()
notEven = []
for i in range(len(s)):
    s[i] = int(s[i])
    if not i % 2:
        notEven.append(s[i])
print(sum(notEven))


# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

set = [2, 3, 4, 5, 6, 2]
rez = []
rez2 = []
set2 = set[:]
set2 = set2[::-1]
for i in range(len(set)):
    set[i] = int(set[i])
    i = 0
while i < (len(set))//2:
    rez.append(set[i])
    i += 1
for j in range(len(set2)):
    set[j] = int(set[j])
    j = 0
while j < (len(set2))//2:
    rez2.append(set2[j])
    j += 1
for item in range(0,len(set)):
    print(rez[item]*rez2[item])

print(set)
print(set2)
print(rez2)
print(rez)


# 3. Задайте список из вещественных чисел. Напишите программу,
#  которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
n_max = 0
n_min = 1000
list = [1.1, 1.2, 3.1, 5, 10.01]

for i in range(len(list)):
    list[i] = list[i]*100
    list[i] = list[i] % 100
    for i in range(len(list)):
        if list[i] > n_max:
            n_max = list[i]
        elif list[i] < n_min and list[i]>0:
            n_min = list[i]

print(list)
print('max =  {n_max}')
print('min = {n_min}')
print('разница между max и min значением :')
print((n_max-n_min)/100)


# 4.  Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

decimalNumber = int(input())
binarNumber = ''
while decimalNumber > 0:
    binarNumber = str(decimalNumber % 2)+binarNumber
    decimalNumber //= 2
print(binarNumber)

# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]
number0 = 0
number1 = 1
number2 = 1

n = int(input('Enter your number  '))

print(number0, number1, number2, end=' ')
while n > 2:
    number0, number1, number2 = number0 + number1, number2, number1 + number2
    print(number0, number2, end=' ')
    n -= 1


