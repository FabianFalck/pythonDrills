#lowercase letters, uppercase letters, numbers, and symbols

#Assume the following minimum requirements:
#- every password has to have 6 sth.
#- every password has to use at least one uppercase letter, one number and one symbol

from random import random
from string import ascii_lowercase
from string import ascii_uppercase
from math import ceil



weak_list = ["Hallo1$", "Gulli5%"]
lower_case_list = ascii_lowercase
upper_case_list = ascii_uppercase
number_list = list(range(1,10))
symbol_list = ["!","$","%","&"]

def pw_length(max_add_num):
    l = int(round(6 + random() * max_add_num))
    return l

def choose_from_list(given_list):
    length_of_list = len(given_list)
    which_item = int(random() * length_of_list - 1)
    return given_list[which_item]

def choose_the_list():
    ran = int(ceil(random()*4))
    chosen = ""
    if(ran == 1):
        chosen = "l"
    if (ran == 2):
        chosen = "u"
    if (ran == 3):
        chosen = "n"
    if (ran == 1):
        chosen = "s"
    return chosen

def main():
    level = input("Please tell me how strong you want your password to be (weak, medium, strong): ")
    length = int()

    if level == "weak":
        return "Your generated password is: " + weak_list[int(ceil(random()*2))]
    elif level == "medium":
        length = pw_length(4)
    elif level == "strong":
        length = pw_length(14) #actually, this is not necessarily a strong password, but we keep it since it's just practising...
    print "length of the password: " + str(length)

    password = []
    itera = range(1,length + 1)
    for i in itera:
        chosen = choose_the_list()
        if chosen == "l":
            password.append(choose_from_list(lower_case_list))
        if chosen == "u":
            password.append(choose_from_list(upper_case_list))
        if chosen == "n":
            password.append(str(choose_from_list(number_list)))
        if chosen == "s":
            password.append(choose_from_list(symbol_list))

    return "Your generated password is: " + ''.join(password)

print main()

#Still occuring errors: 1 pw can be shorter than 6 (eg 5 and 4) 2. length of pw is not correctly used