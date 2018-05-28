balance = 0

while True:
    print("-----------------------------")
    print("1.예금 | 2.출금 | 3.잔고 | 4.종료")
    print("-----------------------------")
    num = input("선택 > ")
    if num.isalpha():
        print("숫자를 입력하세요")
    elif num.isdigit():
        num = int(num)
        if num == 1:
            balance += int(input("예금액 > "))
            continue
        elif num == 2:
            balance -= int(input("출금액 > "))
            continue
        elif num == 3:
            print("잔고액 > {0}".format(balance))
            continue
        elif num == 4:
            print("프로그램 종료")
            break
        else:
            print("다시입력해 주세요")
            continue