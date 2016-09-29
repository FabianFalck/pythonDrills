#check if somebody has won

def check_won(board_status):
    won_bol = False
    won_player = 0

    #check horizontal
    if(board_status[0][0] == board_status[0][1] == board_status[0][2]) and (board_status[0][0] != 0):
        won_bol = True
        if board_status[0][0] == 1:
            won_player = 1
        else:
            won_player = 2
    if(board_status[1][0] == board_status[1][1] == board_status[1][2]) and (board_status[1][0] != 0):
        won_bol = True
        if board_status[1][0] == 1:
            won_player = 1
        else:
            won_player = 2
    if (board_status[2][0] == board_status[2][1] == board_status[2][2]) and (board_status[2][0] != 0):
        won_bol = True
        if board_status[2][0] == 1:
            won_player = 1
        else:
            won_player = 2

    #check vertical
    if (board_status[0][0] == board_status[1][0] == board_status[2][0]) and (board_status[1][0] != 0):
        won_bol = True
        if board_status[1][0] == 1:
            won_player = 1
        else:
            won_player = 2
    if (board_status[0][1] == board_status[1][1] == board_status[2][1]) and (board_status[1][1] != 0):
        won_bol = True
        if board_status[1][1] == 1:
            won_player = 1
        else:
            won_player = 2
    if (board_status[0][2] == board_status[1][2] == board_status[2][2]) and (board_status[1][2] != 0):
        won_bol = True
        if board_status[1][2] == 1:
            won_player = 1
        else:
            won_player = 2
    #check diagonal
    if (board_status[0][0] == board_status[1][1] == board_status[2][2]) and (board_status[1][1] != 0):
        won_bol = True
        if board_status[1][1] == 1:
            won_player = 1
        else:
            won_player = 2

    if (board_status[0][2] == board_status[1][1] == board_status[2][0]) and (board_status[0][2] != 0):
        won_bol = True
        if board_status[0][2] == 1:
            won_player = 1
        else:
            won_player = 2


    return [won_bol, won_player]

winner_is_1 = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

check_won(winner_is_1)