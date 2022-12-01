player1_won = False
player2_won = False

allowed_coordinates = [1,2,3]
board = [['','',''],['','',''],['','','']]

turn_numbers = [1,2,3,4,5]
for i in turn_numbers:
    for row in board:
        print(row)
    print("Player 1's turn")
    while True:
        player1_input_x = int(input('Player 1 turn - x location: ')) - 1
        player1_input_y = int(input('Player 1 turn - y location: ')) - 1
        if board[player1_input_x][player1_input_y] != '':
            print('Invalid. Try again')
        else:
            board[player1_input_x][player1_input_y] = 'X'
            break
    for row in board:
        print(row)
    if board[0][0] == 'X':
        if board[0][1] == 'X' and board[0][2] == 'X':
            player1_won = True
        if board[1][0] == 'X' and board[2][0] == 'X':
            player1_won = True
        if board[1][1] == 'X' and board[2][2] == 'X':
            player1_won = True    
    if player1_won:
        print('Player 1 wins!')
        break

    print("Player 2's turn...")
    while True:
        if i == 5:
            print('Tie!')
            break
        player2_input_x = int(input('x location: ')) - 1
        player2_input_y = int(input('y location: ')) - 1
        if board[player2_input_x][player2_input_y] != '':
            print('Invalid. Try again')
        else:
            board[player2_input_x][player2_input_y] = 'O'
            break
    if board[0][0] == 'O':
        if board[0][1] == 'O' and board[0][2] == 'O':
            player2_won = True
        if board[1][0] == 'O' and board[2][0] == 'O':
            player2_won = True
        if board[1][1] == 'O' and board[2][2] == 'O':
            player2_won = True
    if player2_won:
        print('Player 2 wins!')
        break
