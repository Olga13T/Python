# def dlb(lst: list) -> list:
#     count_dbl = (len(lst) + 1) // 2
#     res_list = [lst[i] * lst[-i - 1] for i in range(count_dbl)]
#     return res_list


# list_1 = [[2, 3, 4, 5], [2, 3, 4, 5, 6]]  ###для тестирования {}
# print(list(map(dlb, list_1)))


# 43. Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# *Пример:*
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]
# count
unic_str = []
# file_path = r'homework4_file.txt'
mystr = [1, 2, 3, 5, 1, 5, 3, 10]
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



#  res = [word for word in my_str.split() if 'абв' not in word]
# list(filter([item for item in (my_list) if my_list.count==1]))


my_list = [1, 2, 3, 5, 1, 5, 3, 10]
# res = []
# for item in my_list:
#     if my_list.count(item) == 1:
#         res.append(item)
# print(res)


res = [item for item in my_list if (my_list.count(item) == 1)]
print(res)

# f = lambda item: my_list.count(item) == 1
# res = list(filter(f, my_list))
# print(res)
