# # 1. Вычислить число c заданной точностью *d*
# #     *Пример:*- при d = 0.001, π = 3.141

# import math

# n = float(input('enter your number accuracy   '))
# i = 0
# while n != 1:
#     n *= 10
#     i += 1
# print(round(math.pi, i))


# # 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# #  Найдите произведение элементов на указанных позициях.
# #  Позиции задаются пользователем с клавиатуры.

# import random

# N = int(input('Введите позицию N: '))

# listNumbers = [random.randint(-N, N) for i in range(10)]
# pozition1 = int(input('Введите позицию первого множителя: '))
# pozition2 = int(input('Введите позицию второго множителя: '))

# print(listNumbers)

# def find_proiz(n1=1, n2=1):

#     for i in range(len(listNumbers)):
#         if n1 == i:
#             n1 = listNumbers[i]
#             print(f"{n1}")
#         if n2 == i:
#             n2 = listNumbers[i]

#             print(f'{n2}')
#     print(n2*n1)

import random
# 5. Реализуйте алгоритм перемешивания списка.

some_list = [random.randint(-20, 30) for i in range(10)]
print(some_list)


res_some_list = random.shuffle(some_list, random)
print(res_some_list)


# из 7го семинара....................
from pathlib import Path
from datetime import datetime


def logg(head='INFO', body='Start program'):
    log_path = Path('data', 'logging.txt')
    log_time = datetime.now().strftime("%Y-%M-%d | %H:%M:%S | ")
    with open(log_path, 'a') as log:
        text = f'{(head + ":"):7}{log_time:30}{body}\n'
        log.write(text)
        # ..........................................................
