#print("hello world")

# переменне, типы переменных Int,float,boolean, None

#value = None
# print(type(value))
# a = 2345
# b = 1.23
# print(type(a))
# print(type(b))
# value = 3465.8
# print(type(value))
# s='hello \nworld' #перенос на новую строку
# print(s)

# import numbers


# numbers = list(range(1, 5))
# print(type(numbers))
# numbers[0] = 10

# for i in numbers:
#     i *= 2
#     print(i)
# print(numbers)
# print(f'{len(numbers)} len')

# colors = ['red','blue','green']
# for e in colors:
#     print(e*2) #redred blueblue greengreen


# colors.append('gray')
# print(colors==['red','blue','green','gray']) #TRUE
# colors.remove('red') # or:   del colors[0]
# print(colors)

def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return          
arg = 1
print(f(arg))
print(type(f(arg)))

# По умолчанию, эти операции применяются к массиву, как если бы он был списком чисел, независимо от его формы. Однако, указав параметр axis, можно применить операцию для указанной оси массива:

# >>>
a.min(axis=0)  # Наименьшее число в каждом столбце
array([1, 2, 3])
a.min(axis=1)  # Наименьшее число в каждой строке
array([1, 4])

# Как уже говорилось, у массива есть форма (shape), определяемая числом элементов вдоль каждой оси:

a
array([[[  0,   1,   2],
        [ 10,  12,  13]],

       [[100, 101, 102],
        [110, 112, 113]]])
a.shape
(2, 2, 3)
