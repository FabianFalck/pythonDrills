#strip() doesn't actually change here anything, since the data is cleaned.
#The error didn't lie in the strip, it was a download problem of the txt file.

prime_numbers = []
happy_numbers = []

with open('PythonDrills/PractisePython/primenumbers.txt','r') as prime_file:
    line = prime_file.readline().strip()
    while line:
        if line != '':
            prime_numbers.append(int(line))
        line = prime_file.readline().strip()

with open('PythonDrills/PractisePython/happynumbers.txt','r') as happy_file:
    print line
    line = happy_file.readline().strip()
    while line:
        if line != '':
            happy_numbers.append(int(line))
        line = happy_file.readline().strip()

print prime_numbers
print happy_numbers

overlap = []

for p in prime_numbers:
    if p in happy_numbers:
        overlap.append(p)
        continue

#using smooth and nice list comprehensions --> try to use them as often as possible
#overlaplist = [elem for elem in primeslist if elem in happieslist]

print overlap