#in this excercise, strip() and split() are neatly explained!

board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
count_moves = 0
turn_of_player = 1
while(count_moves < 9):
    count_moves += 1
    move = input("Hey Player " + str(turn_of_player) + "! Please enter your move as row,col (intuitive, not list style): ")

    move_list = move.split(',')
    row = int(move_list[0])
    col = int(move_list[1])

    if board[row-1][col-1] == 1 or board[row-1][col-1] == 2:
        remove_bol = True
        while remove_bol == True:
            remove_bol = False
            if board[row - 1][col - 1] == 1 or board[row - 1][col - 1] == 2:
                remove_bol = True
                move = input('Already chosen! Please choose again: ')
                move_list = move.split(',')
                row = int(move_list[0])
                col = int(move_list[1])

    board[int(move_list[0]) - 1][int(move_list[1]) - 1] = turn_of_player

    if turn_of_player == 1:
        turn_of_player = 2
    else:
        turn_of_player = 1