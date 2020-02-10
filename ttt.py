# tic tac toe board
ttt_board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]


# prints game board and adds numeration for rows and columns
def print_board(ttt_board):
    print('   0  1  2')
    for i, v in enumerate(ttt_board):
        print(i, v)


# user input, accepts inputs for row and column coordinates from player
def player_move(player=1):
    while True:
        plr_move = input(f'Make your move Player{player}: insert row, column (xy): ')
        try:
            move = []
            for i in plr_move:
                move.append(int(i))
            if ttt_board[move[0]][move[1]] == 0:
                ttt_board[move[0]][move[1]] = int(player)
                break
            else:
                print('Entered slot is already taken')
                return player_move(player)
        except IndexError:
            print(f'Insert row number up to {len(ttt_board) - 1} and column number up to {len(ttt_board[0]) - 1}')
        except ValueError:
            if plr_move == 'quit':
                print('EXIT GAME')
                quit()
            else:
                print(f'Entered {plr_move} is not a valid move, please enter row and column')


# checks whether three elements in a row are the same
def three_in_row(row):
    if row.count(row[0]) == len(row):
        if row[0] != 0:
            return True


# arranges columns to row
def col_to_row(ttt_board, row_count):
    item = []
    for row in ttt_board:
        item.append(row[row_count])
    return item


# arranges diagonal to row
def diag_to_row(ttt_board):
    diag = []
    count = 0
    for row in ttt_board:
        diag.append(row[count])
        count += 1
    return diag


# arranges second diagonal to row
def sec_diag_to_row(ttt_board):
    rcount = len(ttt_board[0]) - 1
    diag = []
    for row in ttt_board:
        diag.append(row[rcount])
        rcount -= 1
    return diag


# checks whether game board is full: if element in ttt_board is 0, returns False
def board_full(ttt_board):
    for row in ttt_board:
        for i in row:
            if i == 0:
                return False


# main function, brings all other functions together
def main():
    print_board(ttt_board)
    not_win = True
    while not_win:
        player = [1, 2]
        for player in player:
            player_move(player)
            print_board(ttt_board)

            # row win condition check
            for row in ttt_board:
                if three_in_row(row) is True:
                    print(f'Player{player} is Row Winner')
                    not_win = False

            # column win condition check
            rcount = 0
            while rcount < len(ttt_board[0]):
                if three_in_row(col_to_row(ttt_board, rcount)) is True:
                    print(f'Player{player} is Column Winner')
                    not_win = False
                    break
                rcount += 1

            # primary diagonal win condition check
            if three_in_row(diag_to_row(ttt_board)) is True:
                print(f'Player{player} is Diagonal Winner')
                not_win = False

            # second diagonal win condition check
            if three_in_row(sec_diag_to_row(ttt_board)) is True:
                print(f'Player{player} is Diagonal Winner')
                not_win = False

            # board full check
            if board_full(ttt_board) is not False:
                not_win = False
                print('Board full')

            # any win condition or board full results in breaking main() while loop and game termination
            if not_win is False:
                print('GAME OVER')
                break


if __name__ == '__main__':
    main()