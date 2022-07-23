#  Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# *Пример:*
# - 6782 -> 23
# - 0,56 -> 11

# from functio8

# Задача №5. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
# Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


import random

def funcwrite(text, spKoff):  # записываем набор коэффициентов в файл
    with open(text, 'w', encoding='utf-8') as file:
        for i in spKoff:
            file.write(f'{i} ')
    return


def funcread(text):  # считываем набор коэффициентов из файла и преобразуем в список int
    spKoff = []
    with open(text, 'r', encoding='utf-8') as file:
        a = file.readline().split(' ')
        for i in range(0, len(a)-1):
            spKoff.append(int(a[i]))
    return spKoff


k = int(input('Введите натуральную степень k = '))  # размер многочлена
spKoff1 = []
spKoff2 = []
for i in range(0, k+1):
    spKoff1.append(random.randint(-10, 10))  # формируем набор коэффициентов
    spKoff2.append(random.randint(-10, 10))  # формируем набор коэффициентов
funcwrite('file1.txt', spKoff1)
funcwrite('file2.txt', spKoff1)
