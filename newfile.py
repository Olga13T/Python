
# # whithout subziro numbers
# number1 = 1
# number2 = 1

# n = int(input('Enter your number  '))

# print(number1, number2, end=' ')
# while n > 2:
#     number1, number2 = number2, number1 + number2
#     print(number2, end=' ')
#     n -= 1


#     def summa(a):
#     if a == 0:
#         return 0
#     elif a == 1:
#         return 1
#     else:
#         return a + summa(a-1)

# rez = summa(10)
# print(rez)


# # fibonacci +
# def fibon(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibon(n-1) + fibon(n-2)

# print(fibon(-1))



# Zadaca s pi
import math

n = float(input('enter your number accuracy   '))
i = 0
while n != 1:
    n = n * 10
    i += 1

print(round(math.pi, i))