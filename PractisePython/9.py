import random

ran_num = random.randint(1,9)

print("The random number is ", ran_num, ", but since you don't know what it is, why am I telling you then?")

guessed = False
guesses_count = 0

while(guessed == False):
    guess = input("Take a guess: ")
    guesses_count = guesses_count + 1

    if(guess == ran_num):
        print "You guessed the correct number!"
        guessed = True
    elif(guess > ran_num):
        print "High off!"
    elif(guess < ran_num):
        print "Low off!"

print "This is the end, man. You needed ", str(guesses_count), " guesses. Try harder next time!"