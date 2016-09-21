#I understood the question differently, yet, this solution is much more complex.

a = [1,1,1,2,2,3,3,4,5,6,7,8,9,10,5,5,6]

def removeDuplicates(l):
    b = []
    for el in l:
        count = 0
        for check in l:
            if el == check:
                count = count + 1
        if count > 1:
            pass
        elif count == 1:
            print el
            b.append(el)
    return b

print removeDuplicates(a)