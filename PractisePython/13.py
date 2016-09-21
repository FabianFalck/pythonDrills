


def fibo():
    how_many = int(input("How long shall the Fibonacci sequence be?"))
    fibo_list = []

    a = 0
    b = 1
    fibo_list.append(b)
    count = 1
    print b
    while count < how_many:
        a, b = b, a + b
        print b
        fibo_list.append(b)
        count = count + 1

    return fibo_list

result = fibo()
print result