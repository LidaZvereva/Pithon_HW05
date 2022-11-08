# 2. Создайте программу для игры в ""Крестики-нолики"".

from random import randint


first_name = input('Введите имя первого игрока: ')
second_name = input('Введите имя второго игрока: ')

print('определим, чей ход.')
rand = randint(1,2)
print(f'Выпало число: {rand}')
if rand % 2 != 0:
    player_1 = first_name
    player_2 = second_name
    print(f'Первым ходит игрок по имени {first_name}. Ваш ход.')
else:
    player_1 = second_name
    player_2 = first_name
    print(f'Первым ходит игрок по имени {second_name}. Ваш ход. ')


mas = [['-' for i in range(3)] for j in range(3)]

def print_mas(print_elem):
    for i in print_elem:
        print(*i)
    return

print_mas(mas)

def you_win(win_pos):
    if win_pos[0][0] == win_pos[0][1] == win_pos[0][2] != '-':
        return win_pos[0][0]
    elif win_pos[1][0] == win_pos[1][1] == win_pos[1][2] != '-':
        return win_pos[1][0]
    elif win_pos[2][0] == win_pos[2][1] == win_pos[2][2] != '-':
        return win_pos[2][0]
    elif win_pos[0][0] == win_pos[1][0] == win_pos[2][0] != '-':
        return win_pos[0][0]
    elif win_pos[0][1] == win_pos[1][1] == win_pos[2][1] != '-':
        return win_pos[0][1]
    elif win_pos[0][2] == win_pos[1][2] == win_pos[2][2] != '-':
        return win_pos[0][2]
    elif win_pos[0][0] == win_pos[1][1] == win_pos[2][2] != '-':
        return win_pos[0][0]
    elif win_pos[2][0] == win_pos[1][1] == win_pos[0][2] != '-':
        return win_pos[2][0]
    else:
        return False


def step(pos, player):
    print(f'Ходит игрок {player}')
    
    st, col = int(input('ряд: ')), int(input('столбец: '))
    
    if pos[st-1][col-1] == 'X' or pos[st-1][col-1] == 'O':
        print('Эта клетка занята, выбирайте другую.')

    elif player == 1:
        pos[st-1][col-1] = 'X'
        print_mas(pos)

    elif player == 2:
        pos[st-1][col-1] = 'O'
        print_mas(pos)
    

count = 0
cur_player = 1

while True:
    step(mas, cur_player)
    win = you_win(mas)
    count += 1
    if win == 'X':
        print(f'Победил(а) {player_1}')
        break
    elif win == 'O':
        print(f'Победил(а) {player_2}')
        break
    elif count == 9:
        print('Ничья')
        break
    if cur_player == 1:
        cur_player = 2
    else:
        cur_player = 1