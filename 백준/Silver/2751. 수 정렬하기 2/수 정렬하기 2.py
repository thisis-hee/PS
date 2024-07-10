import sys

N=int(input())
numbers=list()
for i in range(0,N):
    numbers.append(int(sys.stdin.readline()))

numbers.sort()
for i in range(len(numbers)):
    print(numbers[i])