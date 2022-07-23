#  Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# *Пример:*
# - 6782 -> 23
# - 0,56 -> 11

from functions import input_number_test_float#как и советовали - тяну из файла проверку на число

number = str(input_number_test_float("Enter number : "))

result = 0

# схема - при вводе - проверяет на число, но сам number - строчка.
#  По этому я прохожу по каждому эллементу строки, если число , тогда прибавляю к результату
for i in number:
    if i.isdigit():
        result = result+int(i)

print(f"sum of numbers in {number} = {result}") 

# 3 - Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.

# *Пример:*

# - Для n = 6: {1: 2.0, 2: 2.25, 3: 2.37037037037037, 4: 2.44140625, 5: 2.4883199999999994, 6: 2.5216263717421135}

from functions import input_number_test_biger_then_zero

number_n = input_number_test_biger_then_zero("Enter n : ")

dict_of_numbers = {}

# это мы на семинаре делали, не буду останавилваться 
for i in range(1,number_n+1):
    dict_of_numbers[i] = (1+1/i)**i
print(dict_of_numbers)

result = 0
# а тут высчитывается сумма эллементов , в данном случае for проходится по ключам!! 
for i in dict_of_numbers:
    result += float(dict_of_numbers[i])
print(f"Sum of ellements is {result:.3f}")

# 3. Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой.
str_one ='Говорит попугай попугаю:". Я тебя, попугай, попугаю". Отвечает ему попугай:". Попугай, попугай, попугай!".'
str_two ='попуг'
# str_one = str(input("Enter string 1 : "))
# str_two = str(input("Enter string 2 : "))

count = 0

#print(len(str_one)-len(str_two))
for i in range(0,len(str_one)-len(str_two)):
    #print(str_one[i:i+len(str_two)])
    if str_two.lower() == str_one[i:i+len(str_two)].lower():
        count +=1
print(f"IN {str_one} word {str_two} {count} times")

def input_number_test(text):

    int_test = True
    is_minus = False
    while int_test:
        coord = input(f"{text}")
        if coord[0] == "-":
            is_minus = True
            coord = coord.replace("-","")
        if coord.isdigit():
            coord = int(coord)
            if is_minus:
                coord *= -1
            int_test = False
        else :
            print("Not a number , try again")
    return coord

def input_number_test_not_minus(text):

    int_test = True
    is_minus = False
    while int_test:
        coord = input(f"{text}")
        if coord[0] == "-":
            is_minus = True
            coord = coord.replace("-","")
            print("Entered number < 0 , took +")
        if coord.isdigit():
            coord = int(coord)
            int_test = False
        else :
            print("Not a number , try again")
    return coord 
    


    # polinom
    import numpy as np
import matplotlib.pyplot as plt

coeff = [1., -10., 11., 70.]
res = np.roots(coeff)
import matplotlib.pyplot as plt
ur=np.poly1d(coeff)
x=np.linspace(0,10,100)
y=ur(x)
plt.grid()
plt.plot(x,y)
res

import numpy as np
import matplotlib.pyplot as plt
import math

x = np.linspace(-3, 3, 201)
plt.plot(x, x**2)
plt.plot(x, x**3)
plt.plot(x, x**4)
plt.xlabel('x')
plt.ylabel('y')
plt.asis('tight')
plt.grid(True)
plt.show()