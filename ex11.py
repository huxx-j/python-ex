nums = input("숫자 5개를 , 로 구분하여 입력하세요 > ")

str = nums.split(',')
sum=0
for i in str:
    sum += int(i)

avg = sum/len(str)
print("평균은 {0} 입니다.".format(avg))