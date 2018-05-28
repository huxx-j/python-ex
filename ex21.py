def sum(*args):
    sum = 0
    for i in args:
        print(i)
        sum += i

    print(sum)


sum(0, 3, 17)
