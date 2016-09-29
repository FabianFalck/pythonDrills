def drawboard(kamal):
    kamal = int(kamal)
    i = 0
    ho = "--- "
    ve = "|   "
    ho = ho * kamal
    ve = ve * (kamal+1)
    while i < kamal+1:
        print ho
        if not (i == kamal):
            print ve
        i += 1

def checkGrid(grid):
	# rows
	for x in range(0,3):
		row = set([grid[x][0],grid[x][1],grid[x][2]])
		if len(row) == 1 and grid[x][0] != 0:
			return grid[x][0]

	# columns
	for x in range(0,3):
		column = set([grid[0][x],grid[1][x],grid[2][x]])
		if len(column) == 1 and grid[0][x] != 0:
			return grid[0][x]

	# diagonals
	diag1 = set([grid[0][0],grid[1][1],grid[2][2]])
	diag2 = set([grid[0][2],grid[1][1],grid[2][0]])
	if len(diag1) == 1 or len(diag2) == 1 and grid[1][1] != 0:
		return grid[1][1]

	return 0

def drawboard(board):
    print ('    |   |   ')
    print ('' +board[6]+ '    | ' +board[7]+ '  |   ' +board[8] )
    print ('    |   |   ')
    print ('---------------')
    print ('    |   |   ')
    print ('' +board[3]+ '    | ' +board[4]+ '  | ' +board[5] )
    print ('    |   |   ')
    print('-----------------')
    print ('    |   |   ')
    print ('' +board[0]+ '    | ' +board[1]+ '  |' +board[2] )
    print ('    |   |   ')

drawboard(['', '', '', '', '', '', '', '', ''])



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