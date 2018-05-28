num = input("수를 입력하세요 : ")

if num.isalpha():
    print("숫자가 아닙니다.")
elif num.isdigit():
    if int(num) % 2 == 0:
        print("짝수")
    elif int(num) % 2 == 1:
        print("홀수")
