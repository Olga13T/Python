# r-read
# w
# a

# file_path = r'file.txt'
# # f = open(file_path, 'a')
# # # for line in f:
# # #     print(line, end='')
# # print(f.read())

# # f.close()

# with open(file_path,'w') as f:
#         f.write(str(1,2,3))


# 1. Задайте строку из набора чисел. Напишите программу,
#  которая покажет большее и меньшее число.
#   В качестве символа-разделителя используйте пробел.
# f.decode('cp1251').encode('utf8')

# file_path = r'file.txt'

# with open(file_path, 'r') as f:
#     mystr = f.read()
# mystr = mystr.split()
# for i in range(len(mystr)):
#     mystr[i]=int(mystr[i])
# print(max(mystr))
# print(min(mystr))

# # 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
#     1) с помощью математических формул нахождения корней квадратного уравнения
#     2) с помощью дополнительных библиотек Python
#     disc
#     x1, x2

# file_path = r'file1.txt'
# with open(file_path,'r') as f1:
#     data=f1.read()
# print(f1.read())
# print(data.split())
# data=data[:-2]
# print(data)
# new_data=[int(data[0][:-3]), int((data[1]+data[2])[:-1]),int(data[3]+data[4])]

# d=data[1]**2-4*data[0]*data[2]
# print(d)
# x_1=(-data[1]+d**0.5/(2*data[0]))
# x_2=(-data[1]-d**0.5/(2*data[0]))
# print(x_1,x_2)

# 2. Найдите корни квадратного уравнения
# Ax² + Bx + C = 0
# двумя способами:
#
# 1) с помощью математических формул нахождения корней квадратного уравнения
# альтернативный вариант

# path = 'file.txt'
# with open(path, 'r') as my_file:
#     data = my_file.read()
# data = data.split()
# print(data)
# data = data[:-2]
# print(data)
# data = [int(data[0][:-3]), int((data[1] + data[2])[:-1]), int(data[3] + data[4])]
# print(data)
# # D=b^2-4ac
# d = data[1]**2 - 4 * data[0] * data[2]
# print(d)
# # x=((-b+(d^(1/2)))/(2*a))
# x_1 = (-data[1] + d**0.5) / (2 * data[0])
# x_2 = (-data[1] - d**0.5) / (2 * data[0])
# print(x_1, x_2)

# data = open('ert.txt', 'w')
# data.writelines('\nLesson 5')

# a = int(input('Введите a: '))
# b = int(input('Введите b: '))
# c = int(input('Введите c: '))

# d = b**2-4*c*a
# x1 = (-b+d**0.5)/(2*a)
# x2 = (-b-d**0.5)/(2*a)

# data.writelines(f'\n {a}*x^2+{b}*x+{c}=0 \nx1 = {x1},    \nx2 = {x2}')
# data.close

# alternative method

import math
print('введите коэффициенты для уравнение')
print("ax^2 + bx + c = 0:")
a = float(input("a =  "))
b = float(input("b =  "))
c = float(input("c =  "))

discr = b**2 - 4*a*c
print("Дискриминант D = %.2f" % discr)

if discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2*a)
    x2 = (-b - math.sqrt(discr)) / (2*a)
    print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
elif discr ==0:
    x = -b / (2*a)
    print("x = %.2f" % x)
else:
    print("корней нет")   ###no roots



    
# 3. Задайте два числа. Напишите программу,
#  которая найдёт НОК (наименьшее общее кратное)
#  этих двух чисел.
