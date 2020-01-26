# tictactoe
A game of tic-tac-toe in Python

This is how the field should look like:

```
+-+-+-+
| | | |
+-+-+-+
| | | |
+-+-+-+
| | | |
+-+-+-+

X: Input x, y: > 1, 1
```

After processing the coordinates input for X, it would look like:

```
+-+-+-+
|x| | |
+-+-+-+
| | | |
+-+-+-+
| | | |
+-+-+-+

O: Input x, y: > 1, 1
```

There needs to be validation of input coordinates and a check whether the addressed cell already contains an X or O.

After inserting a symbol into a cell, perform a check whether there is a complete line (horizontal, vertical, or diagonal) of same symbols.

## Step-by-step Guide

1. Write a function `output_field(list_of_cells)` that takes a list of nine elements, and draws the game field as shown above.
    * draw horizontal rulers as a simple `print("+-+-+-+")`
    * draw vertical rulers and cell contents with `str.format()` method, filling cell contents in a loop:
        * each iteration of the loop operates on a 3-element slice of the `list_of_cells` corresponding to the rows
        * the `pattern.format()` pattern contains `"|"`-delimited placeholders for each of the 3 cells of the row 
1. Write a function `input_cell(list_of_cells, party)` that takes two arguments:
    * a list of 9 cells as in previous step,
    * the party (`x` or `o`) whose turn it is
    
    The `input_cell` function:
    * Outputs the party whose turn is expected
    * takes two coordinates from user input (the Python built-in `input()` function) and converts them to `int`
    * checks validity of these coordinates (in range between 1 and 3)
    * checks whether the cell under these coordinates is free yet
    * if so, updates the list of cells with the new value for the cell
    * if not, raises an exception (ValueError) with the problem explanation
    * returns the new `list_of_cells`
1. Write a function `check_lines(list_of_cells, party)` that operates on a list of 9 cells, and checks
    whether there is any of these lines of the same symbols (either `x` or `o`, the `party` argument):
    
    * horizontal line -- any row of cells contain the same symbol
    * vertical line -- any column of cells contain the same symbol
    * diagonal line -- either of two main diagonals 
    
    The function returns True if there is any of such lines on the field.
    
1. Write a function `main()` that would maintain the `list_of_cells` variable and repeatedly do:
    * `output_field()`
    * `input_cell()`
    * `check_lines()`
    
    alternating the `party` between `x` and `o` for each iteration, until a line is found (the `check_lines()` function returns True)
    or the field is full (9 moves have been made).
    
    If the `input_cell()` function raised an exception, this should be handled (the current party is given another try) and the count of moves not updated.
