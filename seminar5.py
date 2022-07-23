# # включения
# # что сделать. что за элемент. условия
# my_str = '1, 22, 54, 76, 2'.split(',')
# #что сделать с элементом, с каким элементом, условие
# my_list = [int(item) for item in my_str if (item > 10)]
# print(my_list)

# f = lambda x: True if x > 10 else False
# my_list = [12, 54, 3, 65]
# res = list(filter(f, my_list))
# print(res)

# my_list_1 = ['A', 'B', 'C', 'D']
# my_list_2 = [15, 76, 1, 98]
# my_list_3 = [65, 68]


# res = list(zip(my_list_1, my_list_2, my_list_3))
# print(res)

# data = list(map(int, input().split()))


# Задача. удалить из исходной строки слова с "абв"
# 'Привет, мир! Мы очеабвнь любим Пайтомаабвба! Семинары'

# str_list = 'Привет, мир! Мы очеабвнь любим Пайтомаабвба! Семинары'
# # str = str.split()
# # print(str)
# # первый вариант
# # str_list = str_list.split()
# def strs(str):
#     for item in str_list:
#         if 'абв' in item:
#             str_list.remove(item)
#     print(str_list)
# # strs(str_list)

# # второй вариант
# res = list(filter(lambda item: 'абв' not in item, str_list.split()))
# print(res)

# s = 'Привет, Мир! Мы очабв любим Пайтонабв! Семинары'
# a = s.split()
# for item  in a:
#     if 'абв' in item:
#         a.remove(item)
# print(a)

# # 1. Удалить из исходной строки все слова с "абв"
# my_str = 'Привет, Мир! Мы очабв любим Пайтонабв! Семинары'
# res = [word for word in my_str.split() if 'абв' not in word]
# print(' '.join(res))
