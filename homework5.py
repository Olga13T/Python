# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

my_list = [word for word in my_list.split() if 'абв' not in word]
list(filter([item for item in (my_list) if my_list.count==1]))

my_list = [1, 2, 3, 5, 1, 5, 3, 10]
res = []
for item in my_list:
    if my_list.count(item) == 1:
        res.append(item)
print(res)

# вариант решения через включения
res = [item for item in my_list if (my_list.count(item) == 1)]
print(res)
# через lambda
f = lambda item: my_list.count(item) == 1
res = list(filter(f, my_list))
print(res)

# 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
# from ast import Break

candy_items = 2021

while candy_items > 0:
    player1 = int(input(' 1 игрок:  '))
    if 0 < player1 <= 28:
        candy_items = candy_items-player1
        print(candy_items)
        if candy_items <= 0:
            print(' 1 Player WIN!!!')
            break
    else:
        player1 = int(input(' 1 игрок:  '))

    player2 = int(input(' 2 игрок :  '))
    if 0 < player2 <= 28:
        candy_items = candy_items-player2
        print(candy_items)
        if candy_items <= 0:
            print(' 2 Player WIN!!!')
    else:
        player2 = int(input(' 2 игрок:  '))
        candy_items = candy_items-player2


# 3.  Создайте программу для игры в ""Крестики-нолики"".
# Работает криво((((
print('Игра крестики  и нолики')

desk = list(range(0, 9))

def draw_desk(desk):
    print('-'*13)
    for i in range(3):
        print('|', desk[0+i*3], '|', desk[1+i*3], '|', desk[2+i*3], '|')
        print('-'*13)

def take_input(player):
    valid = False
    while not valid:
        player_say = input('Выберите позицию на доске:_')
        try:
            player_say = int(player_say)
        except:
            print('Не корректный ввод')
            continue
        if player_say >= 1 and player_say <= 9:
            if(str(desk[player_say-1])
                    not in 'XO'):
                desk[player_say-1] = player
                valid = True
            else:
                print('Данная позиция занята')
        else:
            print('Выберите позицию на доске:_ ')

def check_win(desk):
    win_cards = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                 (1, 4, 7), (2, 5, 8), (0, 4, 8), (6, 4, 2))
    for each in win_cards:
        if desk[each[0]] == desk[each[1]] == desk[each[2]]:
            return desk[each[0]]
        return False

def change_desk(desk):
    count = 0
    win = False
    while not win:
        take_input(desk)
        if count % 2 == 0:
            take_input('X')
        else:
            take_input('O')
        count += 1
        if count > 4:
            temporary = check_win(desk)
            if temporary:
                print(' Вы победили')
                win = True
                break
        if count == 9:
            print('нет победителей')
            break
        
draw_desk(desk)

change_desk(desk)

# 4.  Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# уже не успеваю(((