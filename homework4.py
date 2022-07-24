# 1. Вычислить число c заданной точностью *d*
#     *Пример:*- при d = 0.001, π = 3.141

import math

n = float(input('enter your number accuracy   '))
i = 0
while n != 1:
    n *= 10
    i += 1
print(round(math.pi, i))



# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input('enter your number  '))
i = 1
rez=[]
while i*i <= n:
    if n % i == 0:
        rez.append(i)
        if i!=n//i:
            rez.append(n//i)
    i += 1
rez.sort()
print(rez)


# 3. Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.

unic_str = []
file_path = r'homework4_file.txt'

with open(file_path, 'r') as f:
    mystr = f.read()
mystr = mystr.split()
for i in range(len(mystr)):
    mystr[i] = int(mystr[i])

for i in mystr:
    if mystr.count(i)==1:
        unic_str.append(i)  
print(mystr)
print(unic_str)


# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#     *Пример:*- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# решение ребят разбираю...


# 5. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

path = 'file4_forEx5a.txt'
with open(path, 'r') as my_file:
    data1 = my_file.read()
data1 = data1.split()
print(data1)

path = 'file4_forEx5b.txt'
with open(path, 'r') as file:
    data = file.read()
data = data.split()

print(data)

path = 'fileResult.txt'
with open(path,'w') as result:
    # уже не успевала ко дню сдачи=(((


# 6. Задайте два числа. Напишите программу,
#  которая найдёт НОК (наименьшее общее кратное)
#  этих двух чисел.

num1 = 35
num2 = 14
while num2 > 0:
    num1, num2 = num2, num1 % num2
print(num1)
