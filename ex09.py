data = [1, 3, 5, 8, 9, 11, 15, 19, 18, 20, 30, 33, 31]
count = 0
sum = 0
for i in data:
    if i % 3 == 0:
        count += 1
        sum += i

print("주어진 리스트에서 3의 배수의 개수 => {0}".format(count))
print("주어진 리스트에서 3의 배수의 합 => {0}".format(sum))

