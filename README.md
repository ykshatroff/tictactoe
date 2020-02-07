# tictactoe
A game of tic-tac-toe in Python

New features

1.- New format and resizable board (3-9):

			 ╓━━━━╦━━━━╦━━━━╦━━━━╦━━━━╗
			 │    │    │    │    │    │
			 ╠━━━━╬━━━━╬━━━━╬━━━━╬━━━━╣
			 │    │    │    │    │    │
			 ╠━━━━╬━━━━╬━━━━╬━━━━╬━━━━╣
			 │    │    │    │    │    │
			 ╠━━━━╬━━━━╬━━━━╬━━━━╬━━━━╣
			 │    │    │    │    │    │
			 ╠━━━━╬━━━━╬━━━━╬━━━━╬━━━━╣
			 │    │    │    │    │    │
			 ╚━━━━╩━━━━╩━━━━╩━━━━╩━━━━╝

2.- Encapsulate logic and data in classes:
	classes Board, Player, Msg
3.- Create custom exception: ErrorCellTaken
2.- Use logging to log the match in tictactoe.log
3.- Draw the board with unicode blocks (tkinker next)
4.- Use regular expressions to check the user inputs.
5.- The algorithm to match the lines, use four registers
    for each player:
        1.- rowx (list)
        2.- columny (list)
        3.- first diagonal (int)
        4.- fourth diagonal (int)
    every time that the player input a coordinate, the
    registers are checked and updated if not a line yet.
    Basically when a register value == the size length
    of a line, then we have a line match.


class Msg()

	- It is used only for stdout/stdin messaging, and avoid having
          print(), input() statements everywhere with all those formats 
          characters.
	  
	- It use two dictionaries: 
		- out_msg: to be used with print statements.
		- ask_msg: to be used with input statements.

class Board(line_size)

	- push(x,y,token): Store the last movement in the board.

	- exception_if_cell_is_not_free(x,y): Raise an exception if the cell is taken.

	- is_not_full():   check if there are still free cells in the board.

class Player(line_size, token)

	It mainly store the player token symbol and implement the logic
        to check if it has matched a line within the current movement.

	- xrow(): check if we have a row, if not then update the register
	- ycolumn(): check if we have a column, if not then update the register
	- first_diagonal(): check if we have a first_diagonal, if not then update the register
	- second_diagonal(): check if we have a second_diagonal, if not then update the register
	- coordinates(x,y): update values (x,y) in the instance.

Class ErrorCellTaken

	it is a subclass of Exception and it only implement a custom exception:
	ErrorCellTaken


output_field(Board_obj)
	
	- Draw the board and the tokens
	- Takes a Board object as argument.

input_cell(Board_obj, Player_obj)

	- Get user (x,y) input.
	- Use regular expresion to check if the input string is valid.
	- Handle the exception ErrorCellTaken, which may be raised by
          Board.exception_if_cell_is_not_free(x,y)

check_lines(Player_obj)

	- Take a Player object as argument.
	- Check if any of its methods to check for line matchs return True.

check_if_free_lines(players)

	- It basically tell us if the players has still chances to make
          a line, which is useful information to the user if the board
	  is very big. It would skip the game after the next movement.

ask_line_size()
	
	- Basically it ask to the user the size of the board.
 	- Validate the input with regular expressions.
	- Run an infinite loop until match a valid input.

play_again()

	- It keeps calling main()  as long as the user wants to
	  continue playing.

main()

	- Create the instances:

		- Board -->  board 
		- Player --> player1, player2

	- Manage the execution flow calling:

		- output_field(board)
		- input_cell(board, party)
		- check_lines(party)
		- play_again()
		