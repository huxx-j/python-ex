import random as r

flag = True

while flag:
    hidden = int(r.random() * 100) + 1
    print(hidden)
    print("====================")
    print("  [숫자맞추기게임 시작]  ")
    print("====================")
    while True:
        num = int(input("숫자 > "))
        if num > hidden:
            print("더 낮게")
        elif num < hidden:
            print("더 높게")
        else:
            print("정답입니다.")
            trigger = input("게임을 종료하시겠습니까? (y/n) > ")
            if trigger == 'y':
                break
            elif trigger == 'n':
                print("====================")
                print("  [숫자맞추기게임 종료]  ")
                print("====================")
                flag = False
                break

