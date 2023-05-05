playfield = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]


# описание игры
def instructions():
    print('Игра крестики-нолики')
    print('введите координаты в следующем формате: номер строки, пробел, номер столбца')
    print('побеждает тот, кто первым построит линию из X или 0 в строке, столбце или по диагонали')


# игровая таблица
def showplayfield():
    print('   | 0 | 1 | 2 |')
    print('________________')
    print(f' 0 | {playfield[0][0]} | {playfield[0][1]} | {playfield[0][2]} |')
    print('----------------')
    print(f' 1 | {playfield[1][0]} | {playfield[1][1]} | {playfield[1][2]} |')
    print('----------------')
    print(f' 2 | {playfield[2][0]} | {playfield[2][1]} | {playfield[2][2]} |')
    print('----------------')


# ходы
def moves():
    while True:
        moving = input('сделайте ход: ').split()

        if len(moving) != 2:
            print('Введите номер строки и столбца!')
            continue

        a, b = moving

        if not (a.isdigit()) or not (b.isdigit()):
            print('неверный ввод')
            continue

        a, b = int(a), int(b)

        if 0 > a or a > 2 or 0 > b or b > 2:
            print('введите правильную клетку')
            continue

        if playfield[a][b] != " ":
            print('клетка уже занята')
            continue

        return a, b


# условия, при которых достигается победа
def win():
    win_comb = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for comb in win_comb:
        symbols = []
        for x in comb:
            symbols.append(playfield[x[0]][x[1]])
        if symbols == ["X", "X", "X"]:
            print('Игрок X выиграл')
            return True
        if symbols == ["0", "0", "0"]:
            print('Игрок 0 выиграл')
            return True
    return False


instructions()

# игра
i = 0
while True:
    i += 1
    showplayfield()
    if i % 2 == 1:
        print('Ход X: ')
    else:
        print('Ход 0: ')
    a, b = moves()
    if i % 2 == 1:
        playfield[a][b] = "X"
    else:
        playfield[a][b] = "0"

    if win():
        break
    if i == 9:
        print('ничья')
        break
