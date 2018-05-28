max = 0
for i in range(1, 6, 1):
    if i == 6:
        break
    num = int(input("숫자 : "))
    if max < num:
        max = num

print("최대값은 {0} 입니다.".format(max))
