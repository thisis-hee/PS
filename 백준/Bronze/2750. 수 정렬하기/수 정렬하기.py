N=int(input())
numbers=list()
for i in range(0,N):
    number=int(input())
    if(number not in numbers):
        numbers.append(number)

numbers.sort()
for i in range(len(numbers)):
    print(numbers[i])