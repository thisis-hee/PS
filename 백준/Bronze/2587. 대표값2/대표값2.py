number=list()
for i in range(0,5):
    number.append(int(input()))

number.sort()
print(int(sum(number)/5))
print(number[2])