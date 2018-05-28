num = input("숫자를 입력하세요: ")
sum = 0
if num.isdigit():
    if int(num)%2==0:
        for i in range(2, int(num)+1, 2):
            sum += i
    else:
        for i in range(1, int(num)+1, 2):
            sum += i
    print("결과값 : {0}".format(sum))
elif num.isalpha():
    print("숫자가 아닙니다.")

