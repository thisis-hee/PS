import sys

N=int(input())
numbers=list()

# 수 정렬하기 1과 같이 int(input())으로 받으면 시간 초과됨.
# import sys 후, sys.stdin.readline()으로 받아야 시간초과가 안된다.

for i in range(0,N):
    numbers.append(int(sys.stdin.readline()))

numbers.sort()
for i in range(len(numbers)):
    print(numbers[i])
