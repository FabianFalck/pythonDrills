prime_numbers = []
happy_numbers = []

with open('PythonDrills/PractisePython/primenumbers.txt','r') as prime_file:
    line = prime_file.readline()
    while line:
        prime_numbers.append(int(line))
        line = prime_file.readline()

with open('PythonDrills/PractisePython/happynumbers.txt','r') as happy_file:
    line = happy_file.readline()
    while line:
        happy_numbers.append(int(line))
        line = happy_file.readline()