
contin = True
while(contin == True):
    contin = False

    input_1 = input("Choose r, p or s: ")
    input_2 = input("Choose r, p or s: ")

    if input_1 == "r":
        if input_2 == "r":
            print "Draw, Play again!"
            contin = True
            continue
        if input_2 == "p":
            print "Player 2 wins"
        if input_2 == "s":
            print "Player 1 wins"

    if input_1 == "p":
        if input_2 == "r":
            print "Player 1 wins"
        if input_2 == "p":
            print "Draw, Play again!"
            contin = True
            continue
        if input_2 == "s":
            print "Player 2 wins"

    if input_1 == "s":
        if input_2 == "r":
            print "Player 2 wins"
        if input_2 == "p":
            print "Player 1 wins"
        if input_2 == "s":
            print "Draw, Play again!"
            contin = True
            continue

    again = input("Play again? Answer y or n: ")
    if again == "y":
        contin = True
    else:
        pass #no change