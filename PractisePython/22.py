# reading from a text file

with open('PythonDrills/PractisePython/nameslist.txt','r') as open_file:
    line = open_file.readline().strip('\n')
    dict = {}
    while line:
        dict = countName(line, dict)
        line = open_file.readline().strip('\n')

def countName(line, dict):
    found = False
    line.strip()
    for k, v in dict.items():
        # print 'k: ' + k + 'str(line): ' + str(line)
        if k == str(line):
            dict[str(k)] += 1 # be careful! It is += , not =+
            found = True
            break
        else:
            continue
    if found == False:
        dict[str(line)] = 1

    return dict


print dict