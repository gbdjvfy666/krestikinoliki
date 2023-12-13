board = list(range(1, 10))

wins_options = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]


def do_board():
    print('★★★★★★★★★★')
    for i in range(3):
        print('░', board[0 + i * 3], '░', board[1 + i * 3], '░', board[2 + i * 3], '░')
    print('★★★★★★★★★★')


def take_input(symbol):
    while True:
        value = input('куда поставить: ' + symbol)
        if not (value in '123456789'):
            print('неверный ввод,повторите')
            continue
        value = int(value)
        if str(board[value - 1]) in 'XO':
            print('Эта клетка занята')
            continue
        board[value - 1] = symbol
        break


def check_win():
    for i in wins_options:
        if (board[i[0] - 1]) == (board[i[1] - 1]) == (board[i[2] - 1]):
            return board[i[1] - 1]
    else:
        return False


def global_func():
    c = 0
    while True:
        do_board()
        if c % 2 == 0:
            take_input('X')
        else:
            take_input('O')
        if c > 3:
            win = check_win()
            if win:
                do_board()
                print(win, 'Победа!')
                break
        c += 1
        if c > 8:
            do_board()
            print('Ничья')
            break


global_func()
