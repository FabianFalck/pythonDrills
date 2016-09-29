def tictactoe(repeat):
    game = ''
    one = ''
    two = ''
    for i in range(0,repeat):
        one = one + '  ---'
        two = two + '|    '
    row = one + '\n\n' + two + '|'+ '\n\n'
    for j in range(0, repeat):
        game = game + row
    for h in range(0, repeat):
        game = game + '  ---'
    print game

tictactoe(10)

