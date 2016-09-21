import random

def main():

    cows_count = 0
    bulls_count = 0

    while(cows_count < 4):

        random_number = str()
        for i in range(1,5):
            if i == 1:
                new = random.randint(1,9)
            else:
                new = random.randint(0,9)
            random_number = random_number + str(new)
        random_number = int(random_number)

        print "The random number is: " + str(random_number)

        random_number_string = str(random_number)
        random_number_list = [int(i) for i in random_number_string]

        cows_count = 0
        bulls_count = 0

        guessed_number = input("Please guess the 4-digit number: ")
        guessed_number_string = str(guessed_number)
        guessed_number_list = [int(i) for i in guessed_number_string]

        for i ,num in enumerate(random_number_list):
            if num == guessed_number_list[i]:
                cows_count = cows_count +  1
            else:
                for num_one in random_number_list:
                    if num_one == guessed_number_list[i]:
                        bulls_count = bulls_count + 1
                        break

        print "You have " + str(cows_count) + " cows and " + str(bulls_count) + " bulls."

main()

#cow when exactly right, bull when just the number right (not overlapping)




