import itertools
import re
import logging

logging.basicConfig(filename='tictactoe.log',
                    filemode='a',
                    format='%(asctime)s - %(message)s - %(processName)s - %(levelname)s',
                    datefmt='%d-%b-%y %H:%M:%S ',
                    level=logging.DEBUG)

class Msg():

    def out(self, code, arg="_out_?"):

        out_msg = {
            "tictactoe": """\t\n       ·· T I C - T A C - T O E ··       
                            \t\n              ~  the game  ~        """,

            "full_board": "\n\t The board is full.\n",

            "win": f"\n\n\t Player {arg}, matched a line!! Congratulations!!",

            "bye": "\n\t Bye! see you soon!",

            "No chances": "\n\t There is not chances left, match finished. \n",

            "Wrong format": ("\n\t Wrong format, please use this format: x,y"
                             "\n\t And introduce only numeric coordinates."
                             "\n\t For example: 1,3"
                             f"\n\t The maximun value for each coordenate is: {arg}"),

            "Wrong: line size": ("\n\t This is not a valid entry."
                                 "\n\t Please choose a numeric value on this range (3-9): "),

            "Player_quit": f"\n\t Player {arg} quit. ",

            "Cell already taken": f"\n\t This cell {arg} is already taken."
                                  "\n\t Please choose another cell."
        }

        ask_msg = {
            "line size?": "\n\t Please introduce the line size (3-9): ",

            "Play again?": "\n\t Do you wanna play again? (y/n): ",

            "x,y?": f"\n\tType (quit) to exit\n\t {arg}: Input x, y: > "
        }

        if code[-1] == "?":                        # use input() when the code key finish with "?"
            return input(ask_msg.get(code))
        else:
            print(out_msg.get(code))               # otherwise use print()


class Board:
    def __init__(self, line_size):
        self.line_size = line_size
        self.initializer = " " * 4
        self.number_of_cells = int(line_size) ** 2
        self.cells = [self.initializer] * self.number_of_cells
        self.filled_cells = []
        self.movements_left = self.number_of_cells  # Movements left to full fill the board

    def __repr__(self, index):
        return self.cells[index]

    def push(self, x, y, token):

        lineal_index = self.__xy_to_index__(x, y)    # Convert coordinates to lineal index
        self.cells[lineal_index] = " " + token + " " * 2
        self.filled_cells.append(lineal_index)
        self.movements_left -= 1

    def exception_if_cell_is_not_free(self, x, y):
    # Raise an exception if cell (x,y) is not free

        lineal_index = self.__xy_to_index__(x, y)

        if lineal_index in self.filled_cells:
            raise ErrorCellTaken


    def is_not_full(self):

        if self.movements_left == 0:
            return False
        return True

    def __xy_to_index__(self, x, y):
        # f(x,y,z) = x + z(y - 1) - offset
        # z: sqrt(square matrix size)
        # x,y:  coordinates (1,1) left superior corner

        offset = 1  # board first index is (1,1) but list first index is (0)
        z = self.line_size  # just the size of a column or a row in this "square matrix"
        lineal_index = x + z * (y - 1) - offset
        return lineal_index


class Player:
    # It mainly store the player token symbol and implement the logic
    # to check if has matched a line within the current movement.

    def __init__(self, line_size, token):

        self.line_size = line_size
        self.row = [0] * line_size
        self.column = [0] * line_size
        self.first_diagonal = 0
        self.second_diagonal = 0
        self.token = token
        self.last_x = 0
        self.last_y = 0
        self.offset = 1

    def __repr__(self):
        return self.token

    def xrow(self):
        # it record the number of tokens that the player has on each row
        # when the number of tokens == line_size  it means it did a line.
        # Before updating the last movement it if check if the counter is
        # already line_size - 1 (then it return true) if no, then it update
        # the counter.

        if self.row[self.last_x] == (self.line_size - 1):
            return True
        else:
            self.row[self.last_x] += 1
            return False

    def ycolumn(self):
        #  the same algorithm used in xrow, but now on columns.

        if self.column[self.last_y] == (self.line_size - 1):
            return True
        else:
            self.column[self.last_y] += 1
            return False

    def first_diag(self):
        # It increase a counter when we write in the first diagonal
        # We are in the first diagonal when x=y
        # if the counter reach line_size then it means a line match
        # Before updating the counter it check if line_size -1 then
        # it return True, if not then update the counter.

        if self.last_x == self.last_y:
            if self.first_diagonal == (self.line_size - 1):
                return True
            else:
                self.first_diagonal += 1
                return False
        else:
            return False

    def second_diag(self):
        # We are in the second diagonal when:
        # x + y = line_size + 1
        # we have a line when the token counter = line_size
        # but we read the counter before updating its value
        # if the value is (line_size -1) it returns True
        # otherwise it update the register and return False.

        if ((self.last_x + self.last_y) + 2 * self.offset) == (self.line_size + 1):

            if self.second_diagonal == (self.line_size - 1):
                return True
            else:
                self.second_diagonal += 1

                return False
        else:
            return False

    def coordinates(self, x, y):
        # offset, if the user notation has internally another value.
        # For example: user input (1,1) -->  (0,0) internal value

        self.last_x = x - self.offset
        self.last_y = y - self.offset

class ErrorCellTaken(Exception):

    def __init__(self):
        Exception.__init__(self, "\n\tError: The user tried to use a taken cell")

def output_field(board):

    def draw_block(axis):
        tabs = 3
        print("\t" * tabs, axis)

    slc = "\U00002553"  # superior left corner
    h = "\U00002501"  # clean horizontal line
    hdj = "\U00002566"  # horizontal down junction
    src = "\U00002557"  # superior right corner.
    v = "\U00002502"  # clean vertical line
    vjl = "\U00002560"  # vertical junction left
    c = "\U0000256C"  # cross
    vjr = "\U00002563"  # vertical junction right
    ilc = "\U0000255A"  # inferior left corner
    irc = "\U0000255D"  # inferior right corner
    huj = "\U00002569"  # horizontal up junction

    h_line = slc + h * 2 + (h * 2 + hdj + h * 2) * (board.line_size - 1) + h * 2 + src
    draw_block(h_line)

    for i in range(0, board.number_of_cells):
        if i % board.line_size == 0:

            v_line = v + v.join(board.cells[i:(i + board.line_size)]) + v
            h_line = vjl + h * 2 + (h * 2 + c + h * 2) * (board.line_size - 1) + h * 2 + vjr
            draw_block(v_line)

            if i < int(board.number_of_cells - board.line_size):
                draw_block(h_line)

    h_line = ilc + h * 2 + (h * 2 + huj + h * 2) * (board.line_size - 1) + h * 2 + irc
    draw_block(h_line)


def input_cell(board, party):
    message = Msg()

    while True:
        coord = message.out("x,y?", party)
        if coord.upper() == "QUIT":
            return None

        lenght = board.line_size

        if re.fullmatch(f"[1-{lenght}],[1-{lenght}]", coord) != None:

            x, y = coord.split(",")
            x, y = int(x), int(y)

            try:
                board.exception_if_cell_is_not_free(x, y)

            except ErrorCellTaken:

                message.out("Cell already taken", f"({x},{y})")
                logging.info(f"Player {party} Error (cell already taken {x},{ y})")
            else:
                break
        else:
            message.out("Wrong format", board.line_size)
            logging.info(f"Player {party} Error (typed wrong format: {coord})")

    party.coordinates(x, y)
    logging.info(f"Player {party} move ({x},{ y})")

    board.push(x, y, str(party))

    output_field(board)

    return True

def check_lines(party):
    if any([party.xrow(), party.ycolumn(), party.first_diag(), party.second_diag()]):
        return True
    else:
        return False

def check_if_free_lines(players):
    # if every player has at least a token in:
    #  1) every row and column
    #  2) every diagonal
    # then it is not possible to match a line anymore.

    # We keep a register for every row in which the player
    # has a token. So, the value of the register is the
    # number of tokens on that row. If the numbers of
    # registers match the dimention to make a line it means
    # that the user has a token in all the rows of that
    # board.

    # The same for columns

    line_size = len([item for item in players[0].row])

    for i in range(line_size):
        if not (players[0].row[i] and players[1].row[i]):
            return True
        if not (players[0].column[i] and players[1].column[i]):
            return True

    # We have two diagonal registers to to keep the number of
    # tokens in first diagonal and second diagonal
    # Both were initialized to cero.
    # While it doesnt have a token in the diagonal it value will
    # remain cero what means that the diagonal is not BLOCKED YET
    # to the OTHER PLAYER. So it is possible still to make
    # a line on this diagonal


    if 0 in [x.first_diagonal for x in players]:   # FIRST DIAGONAL
        return True

    if 0 in [x.second_diagonal for x in players]:  # SECOND DIAGONAL
        return True

    return False


def ask_line_size():
    message = Msg()

    while True:
        line_size = message.out("line size?")
        if re.fullmatch("[3-9]", line_size):
            return int(line_size)
        message.out("Wrong: line size")


def play_again():
    message = Msg()
    play_again = message.out("Play again?")
    if play_again.upper() == "Y":
        main()
    else:
        message.out("bye")
        logging.info(f" ***** Finish the match *****")


def main():

    message = Msg()
    logging.info("***** Start the match ****")

    message.out("tictactoe")
    line_size = ask_line_size()
    logging.info(f"line size: {line_size}")

    board = Board(line_size)

    player1 = Player(board.line_size, "X")
    player2 = Player(board.line_size, "O")

    players = [player1, player2]

    turn = itertools.cycle(players)  # infinite iterator to switch players.

    output_field(board)

    while board.is_not_full:

        party = next(turn)
        logging.info(f"Player {party} turn #")

        if input_cell(board, party) == None:
            message.out("Player_quit", party)
            logging.info(f"Player {party} quit")
            break

        if check_lines(party):
            message.out("win", party)
            logging.info(f"Player {party} win!!!")
            break
    else:
        message.out("full_board")
        logging.info(f"Full table")

    play_again()

if __name__ == "__main__":

    main()



