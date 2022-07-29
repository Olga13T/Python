# count_cnd = 2021
# кто ходит = 1
# Цикл пока у нас есть конфеты:
#     предлагать игрокам по очереди брать конфеты от 1 до 28, проверяя, кто сейчас ходит
#     сколько конфет осталось
#     если конфет нет, то выйти из цикла и сказать кто победил
#     иначе передаь ход другому
# google meet dickord

# from ast import Break

# candy_items = 89

# while candy_items > 0:
#     player1 = int(input(' 1 игрок:  '))
#     if 0 < player1 <= 28:
#         candy_items = candy_items-player1
#         print(candy_items)
#         if candy_items <= 0:
#             print(' 1 Player WIN!!!')
#             Break
#     else:
#         player1 = int(input(' 1 игрок:  '))

#     player2 = int(input(' 2 игрок :  '))
#     if 0 < player2 <= 28:
#         candy_items = candy_items-player2
#         print(candy_items)
#         if candy_items <= 0:
#             print(' 2 Player WIN!!!')
#     else:
#         player2 = int(input(' 2 игрок:  '))
#         candy_items = candy_items-player2

# X and O _ GAME
# player1 = Х
# player2 = 0
# desk = [[], [],[]]
# win_player1 = {[1,2,2],
#                 [2,1,2],
#                 [2,2,1]},{[2,1,2],
#                         [2,1,2],
#                         [2,1,2]}


#  res = [word for word in my_str.split() if 'абв' not in word]
# list(filter([item for item in (my_list) if my_list.count==1]))


# my_list = [1, 2, 3, 5, 1, 5, 3, 10]
# res = []
# for item in my_list:
#     if my_list.count(item) == 1:
#         res.append(item)
# print(res)


# res = [item for item in my_list if (my_list.count(item) == 1)]
# print(res)

# f = lambda item: my_list.count(item) == 1
# res = list(filter(f, my_list))
# print(res)

# 1. Задайте список из нескольких чисел.
#  Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# s = input('enter list:  ').split()
# notEven = []
# for i in range(len(s)):
#     s[i] = int(s[i])
#     if not i % 2:
#         notEven.append(s[i])
# print(sum(notEven))
from operator import indexOf

#    0  1  2  3  4  5  6  
s = [2, 3, 5, 3, 6, 4, 8]

# rez = [i%2!= 0 for i in s ]
# print(rez)
res = [item for item in s if not (s.index(item) % 2 == 0)]
print(res)
