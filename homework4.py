# 1. Вычислить число c заданной точностью *d*
#     *Пример:*- при d = 0.001, π = 3.141

# import math

# n = float(input('enter your number accuracy   '))
# i = 0
# while n != 1:
#     n *= 10
#     i += 1
# print(round(math.pi, i))



# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# n = int(input('enter your number  '))
# i = 1
# rez=[]
# while i*i <= n:
#     if n % i == 0:
#         rez.append(i)
#         if i!=n//i:
#             rez.append(n//i)
#     i += 1
# rez.sort()
# print(rez)


# 3. Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.

# unic_str = []
# file_path = r'homework4_file.txt'

# with open(file_path, 'r') as f:
#     mystr = f.read()
# mystr = mystr.split()
# for i in range(len(mystr)):
#     mystr[i] = int(mystr[i])

# for i in mystr:
#     if mystr.count(i)==1:
#         unic_str.append(i)  
# print(mystr)
# print(unic_str)


# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#     *Пример:*- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

def create_mnogoch(x1_values, i):
    def mnogoch(x1):
        divider = 1
        rez=1
        for j in range(len(x1_values)):
            if j !=i:
                rez *=(x1-x1_values[j])
                divider*=(x1_values[i]-x1_values[j])
        return rez/divider
    return mnogoch

def create_dlin_mnogoch(x1_values,x2_values):
    mnogoch = []
    for i in range(len(x1_values)):
        mnogoch.append(create_mnogoch(x1_values,i))
    def dlin_mnogoch(x1):
        rez = 0
        for i in range(len(x2_values)):
            rez +=x2_values[i]*mnogoch[i](x1)
        return rez
    return dlin_mnogoch
x1_values = [0, 2, 3, 5]
x2_values = [0,1, 3, 2]

new_mnog= create_dlin_mnogoch(x1_values, x2_values)

for x in x1_values:
    print("x1 = {:.4f}\t x2 = {:4f}".format(x,new_mnog(x)))


# 5. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.



# 6. Задайте два числа. Напишите программу,
#  которая найдёт НОК (наименьшее общее кратное)
#  этих двух чисел.

# доделать с чтением из файла все задания из хв4!!!!!

# num1 = 35
# num2 = 14
# while num2 > 0:
#     num1, num2 = num2, num1 % num2
# print(num1)
