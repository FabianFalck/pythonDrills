# reading from a text file

with open('PythonDrills/PractisePython/Training_01.txt','r') as open_file:
    line = open_file.readline().strip('\n')
    dict = {}
    while line:
        count_hor = 0
        line_stripped = ''
        for s in line:
            if s == '/':
                count_hor += 1
            if (count_hor == 2) and (s != '/'):
                line_stripped = line_stripped + s

        dict = countName(line_stripped, dict)
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