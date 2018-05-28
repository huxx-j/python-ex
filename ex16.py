num = int(input("금액을 입력하세요 > "))

data = [50000, 10000, 5000, 1000, 500, 100, 50, 10, 5, 1]

for i in data:
    c = int(num / i)
    num -= i * c
    print("{0}원: {1}개".format(i, c))
