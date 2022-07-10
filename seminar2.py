# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.

#     *Пример:*

# - Для N = 5: 1, -3, 9, -27, 81
# def searchNumber(1

# ****
# def func(x):
#     s = 1
#     print(s, end=' ')
#     for i in range(1, x):
#         s = s*(-3)
#         print(s, end=' ')


# n = int(input('--> '))
# func(n)
# ***
# ****
# def Proiz(a, n)
# while n > 0:
# # a[1]=1
# # a[2]=a[1]*(-3)
# a[n]=a[n-1]*(-3)

# Proiz(1,5)
# def returnSequence(num):
#     prod = 1
#     print(prod, end = ' ')
#     for _ in range(num - 1):
#         prod *= -3
#         print(f"{prod} ", end = '')

# returnSequence(int(input("Please, input number ")))

# def searchNumber(a, b):
#     for i in range(a):
#         print(b)
#         b *= -3

# n = int(input('Введите число: '))
# result = 1
# searchNumber(n, result)

# def print_numbers(x):
#     vivod = 1
#     for i in range(x):
#         print(vivod, end=' ')
#         vivod = vivod * -3

# n = int(input('--> '))
# print_numbers(n)

# def print_numbers(x=[]):
#     x.append(5)
#     print(x)
#  особенность в питоне:
# a = []
# print_numbers(x=a)
# print_numbers(x=a)
# print_numbers(x=a)
# print_numbers(x=a)
# print(f'---> {a}')

# Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.

st1 = 'привет, мир, т, привет!'
st2 = ','
def str(st1, st2):
    t = 0
    for i in range(len(st1) - len(st2)):
        if (st1[i : i + len(st2)] == st2):
            t += 1
    return t
print(str(st1, st2))


# def find_line(string:str, under_strind:str):
#     print(string.count(under_strind))

# user_string = input('Введите текст: ')
# user_understring = input('Введите текст: ')
# find_line(user_string, user_understring)




symbol = 'so'
base_string = 'some pernal'
position = 0
qty = 0
while(True):
    position = base_string.find(symbol, position)
    if position == -1:
        break
    else:
        position += 1    # как вариант len(symbol)
        qty += 1
print(qty)
