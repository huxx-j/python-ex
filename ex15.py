for i in range(1, 100, 1):

    if i % 10 == 3 or i % 10 == 6 or i % 10 == 9 or i // 10 == 3 or i // 10 == 6 or i // 10 == 9:
        print("{0} 짝".format(i), end="")
        if i // 10 == 3 or i // 10 == 6 or i // 10 == 9:
            if i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
                print("짝")
            else:
                print()
        else:
            print()
