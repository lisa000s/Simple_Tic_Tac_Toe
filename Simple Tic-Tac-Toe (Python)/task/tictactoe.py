symbols = '_________'
grid1 = list(symbols[0:3].replace('_',' '))
grid2 = list(symbols[3:6].replace('_',' '))
grid3 = list(symbols[6:9].replace('_',' '))
global winner

def print_result():
    global winner
    draw = True
    impossible = False
    winner_found = False
    X_count = symbols.count('X')
    O_count = symbols.count('O')
    if abs(X_count - O_count) >= 2:
        impossible = True
        print("Impossible")
    else:
        # check diagonal win
        move = grid1[0]
        if grid1[0] == move and grid2[1] == move and grid3[2] == move:
            draw = False
            winner = move
            winner_found = True
        move = grid1[2]
        if grid1[2] == move and grid2[1] == move and grid3[0] == move:
            draw = False
            if winner_found is True:
                if winner != move:
                    impossible = True
                    print("Impossible")
            else:
                winner_found = True
                winner = move
        # check vertical win
        move = grid1[0]
        if grid1[0] == move and grid2[0] == move and grid3[0] == move:
            draw = False
            if winner_found is True:
                if winner != move:
                    impossible = True
                    print("Impossible")
            else:
                winner_found = True
                winner = move
        move = grid1[1]
        if grid1[1] == move and grid2[1] == move and grid3[1] == move:
            draw = False
            if winner_found is True:
                if winner != move:
                    impossible = True
                    print("Impossible")
            else:
                winner_found = True
                winner = move
        move = grid1[2]
        if grid1[2] == move and grid2[2] == move and grid3[2] == move:
            draw = False
            if winner_found is True:
                if winner != move:
                    impossible = True
                    print("Impossible")
            else:
                winner_found = True
                winner = move
        # check horizontal win
        move = grid1[0]
        if grid1[0] == move and grid1[1] == move and grid1[2] == move:
            draw = False
            if winner_found is True:
                if winner != move:
                    impossible = True
                    print("Impossible")
            else:
                winner_found = True
                winner = move
        move = grid2[0]
        if grid2[0] == move and grid2[1] == move and grid2[2] == move:
            draw = False
            if winner_found is True:
                if winner != move:
                    impossible = True
                    print("Impossible")
            else:
                winner_found = True
                winner = move
        move = grid3[0]
        if grid3[0] == move and grid3[1] == move and grid3[2] == move:
            draw = False
            if winner_found is True:
                if winner != move:
                    impossible = True
                    print("Impossible")
            else:
                winner_found = True
                winner = move
        if draw is False and impossible is False:
            if winner != '_' :
                print('{} wins'.format(winner))
        # check draw
        if symbols.count('_') == 0 and draw is True:
            print('Draw')
        # check game not finished
        if symbols.count('_') > 0 and winner_found is False:
            print('Game not finished')

def print_grid():
    print('---------')
    for i in range(len(grid1)):
        if i == 0:
            print('|', grid1[i], '', end='')
        elif i == 2:
            print(grid1[i],'|',end='')
        else:
            print(grid1[i],'', end='')
    print()
    for i in range(len(grid2)):
        if i == 0:
            print('|', grid2[i], '', end='')
        elif i == 2:
            print(grid2[i],'|',end='')
        else:
            print(grid2[i],'', end='')
    print()
    for i in range(len(grid3)):
        if i == 0:
            print('|', grid3[i], '', end='')
        elif i == 2:
            print(grid3[i],'|',end='')
        else:
            print(grid3[i],'', end='')
    print('\n---------')

def get_symbol(grid1, grid2, grid3):
    symbols = grid1 + grid2 + grid3
    symbol_len = len(symbols) - symbols.count(' ')
    # print(symbols)
    # print(symbol_len)
    if symbol_len == 0 or symbol_len % 2 == 0:
        return 'X'
    else:
        return 'O'


print_grid()
check1_error = False
check2_error = False
valid_move = False
winner_found = False
while winner_found is False and not check1_error or valid_move is False or grid1.count(' ') != 0 or grid2.count(' ') != 0 or grid3.count(' ') != 0:
    check1_error = False
    move = input()
    get_symbol(grid1, grid2, grid3)
    for i in move.split(' '):
        if not i.isdigit():
            print("You should enter numbers!")
            check1_error = True
            break
        if int(i) > 3 or int(i) < 1:
            print("Coordinates should be from 1 to 3!")
            check1_error = True
            check2_error = False
            continue
    while check1_error is not True and check2_error is not True:
        # (1, 1)
        if move == '1 1':
            if grid1[0] == ' ':
                grid1[0] = get_symbol(grid1, grid2, grid3)
                # if grid1.count('X') % 2 == 0:
                #     grid1[0] = 'X'
                # else:
                #     grid1[0] = 'O'
                valid_move = True
            else:
                print("This cell is occupied! Choose another one!")
                check2_error = True
                continue
        # (1, 2)
        if move == '1 2':
            if grid1[1] == ' ':
                grid1[1] = get_symbol(grid1, grid2, grid3)
                valid_move = True
            else:
                print("This cell is occupied! Choose another one!")
                check2_error = True
                continue
        # (1, 3)
        if move == '1 3':
            if grid1[2] == ' ':
                grid1[2] = get_symbol(grid1, grid2, grid3)
                valid_move = True
            else:
                print("This cell is occupied! Choose another one!")
                check2_error = True
                continue
        # (2, 1)
        if move == '2 1':
            if grid2[0] == ' ':
                grid2[0] = get_symbol(grid1, grid2, grid3)
                valid_move = True
            else:
                print("This cell is occupied! Choose another one!")
                check2_error = True
                continue
        # (2, 2)
        if move == '2 2':
            if grid2[1] == ' ':
                grid2[1] = get_symbol(grid1, grid2, grid3)
                valid_move = True
            else:
                print("This cell is occupied! Choose another one!")
                check2_error = True
                continue
        # (2, 3)
        if move == '2 3':
            if grid2[2] == ' ':
                grid2[2] = get_symbol(grid1, grid2, grid3)
                valid_move = True
            else:
                print("This cell is occupied! Choose another one!")
                check2_error = True
                continue
        # (3, 1)
        if move == '3 1':
            if grid3[0] == ' ':
                grid3[0] = get_symbol(grid1, grid2, grid3)
                valid_move = True
            else:
                print("This cell is occupied! Choose another one!")
                check2_error = True
                continue
        # (3, 2)
        if move == '3 2':
            if grid3[1] == ' ':
                grid3[1] = get_symbol(grid1, grid2, grid3)
                valid_move = True
            else:
                print("This cell is occupied! Choose another one!")
                check2_error = True
                continue
        # (3, 3)
        if move == '3 3':
            if grid3[2] == ' ':
                grid3[2] = get_symbol(grid1, grid2, grid3)
                valid_move = True
            else:
                print("This cell is occupied! Choose another one!")
                check2_error = True
                continue
        if check1_error is not True:
            print_grid()
        break
    draw = True
    impossible = False
    symbols = grid1 + grid2 + grid3
    X_count = symbols.count('X')
    O_count = symbols.count('O')
    if abs(X_count - O_count) >= 2:
        impossible = True
        print("Impossible")
    else:
        # check diagonal win
        move = grid1[0]
        if move != ' ' and grid1[0] == move and grid2[1] == move and grid3[2] == move:
            draw = False
            winner = move
            winner_found = True
        move = grid1[2]
        if move != ' ' and grid1[2] == move and grid2[1] == move and grid3[0] == move:
            draw = False
            if winner_found is True:
                if winner != move:
                    impossible = True
                    print("Impossible")
            else:
                winner_found = True
                winner = move
        # check vertical win
        move = grid1[0]
        if move != ' ' and grid1[0] == move and grid2[0] == move and grid3[0] == move:
            draw = False
            if winner_found is True:
                if winner != move:
                    impossible = True
                    print("Impossible")
            else:
                winner_found = True
                winner = move
        move = grid1[1]
        if move != ' ' and grid1[1] == move and grid2[1] == move and grid3[1] == move:
            draw = False
            if winner_found is True:
                if winner != move:
                    impossible = True
                    print("Impossible")
            else:
                winner_found = True
                winner = move
        move = grid1[2]
        if move != ' ' and grid1[2] == move and grid2[2] == move and grid3[2] == move:
            draw = False
            if winner_found is True:
                if winner != move:
                    impossible = True
                    print("Impossible")
            else:
                winner_found = True
                winner = move
        # check horizontal win
        move = grid1[0]
        if move != ' ' and grid1[0] == move and grid1[1] == move and grid1[2] == move:
            draw = False
            if winner_found is True:
                if winner != move:
                    impossible = True
                    print("Impossible")
            else:
                winner_found = True
                winner = move
        move = grid2[0]
        if move != ' ' and grid2[0] == move and grid2[1] == move and grid2[2] == move:
            draw = False
            if winner_found is True:
                if winner != move:
                    impossible = True
                    print("Impossible")
            else:
                winner_found = True
                winner = move
        move = grid3[0]
        if move != ' ' and grid3[0] == move and grid3[1] == move and grid3[2] == move:
            draw = False
            if winner_found is True:
                if winner != move:
                    impossible = True
                    print("Impossible")
            else:
                winner_found = True
                winner = move
        if draw is False and impossible is False and winner_found is True:
            if winner != ' ':
                print('{} wins'.format(winner))
                break
        # check draw
        if symbols.count(' ') == 0 and draw is True:
            print('Draw')
            break

