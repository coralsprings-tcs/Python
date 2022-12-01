# Tic-Tac-Toe
* Try getting a game of tic-tac-toe made using just input, print, and lists.
* The following board gives an idea of how.
```
(1,1) || (1,2) || (1,3)
=======================
(2,1) || (2,2) || (2,3)
=======================
(3,1) || (3,2) || (3,3)
```
where (1,1),(1,2)...(3,2),(3,3) are your coordinates in (x,y)
It can be made using lists where

```python
coordinate_x_y[0] = x_value
coordinate_x_y[1] = y_value
```
(ie. coordinate_1_2, coordinate_3_3)

In other words every player turn (player 1 has a maximum of 5 and player 2 has a maximum of 4) you will have to:
* Ask for a position
* Update that position

Use the following template will help but feel free to make your own.
```python
player1_won = False
player2_won = False

allowed_coordinates = [1,2,3]
board = [['','',''],['','',''],['','','']]

turn_numbers = [1,2,3,4,5]
for i in turn_numbers:
    # print board
    print("Player 1's turn")
    while True:
        # player 1 stuff goes here
        # if correct input (valid space and not already used):
            # break
    # print board
    if board[0][0] == 'X':
        if board[0][1] == 'X' and board[0][2] == 'X':
            player1_won = True
        if board[1][0] == 'X' and board[2][0] == 'X':
            player1_won = True
        if board[1][1] == 'X' and board[2][2] == 'X':
            player1_won = True    
    if player1_won:
        # what happens when player 1 wins (you can break from here to stop)
    print("Player 2's turn...")
    while True:
        # player 2 stuff goes here
        # if correct input (valid space and not already used):
            # break
    if board[0][0] == 'O':
        if board[0][1] == 'O' and board[0][2] == 'O':
            player2_won = True
        if board[1][0] == 'O' and board[2][0] == 'O':
            player2_won = True
        if board[1][1] == 'O' and board[2][2] == 'O':
            player2_won = True
    if player2_won:
        # what happens when player 1 wins (you can break from here to stop)
```

HINT 1: Convert your input to a number with int() such as below
 ```python
input_int = int(input('Enter a number: '))
print(input_int+5)
```
HINT2: Lists start with index 0 so list[0] will be your first item for list.

Compare to tictactoe.py at the end.
