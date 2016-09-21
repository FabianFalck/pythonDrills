import math

num = input("Give me some number I shall find all divisors of: ")

test_range = range(1, int(math.ceil(num/2))+1) #range is off by one! mind that!
print("Test Range: ", test_range)
divisors = []

for pot in test_range:
    if num % pot == 0:
        divisors.append(pot)

divisors.append(num)

print("Ok, here is a list of all divisors of ",num, " : ", divisors)


