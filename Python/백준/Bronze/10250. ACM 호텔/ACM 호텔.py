import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())
    if (N % H == 0):
        floor = H
        num = N // H
        print(floor * 100 + num)
    else:
        floor = N % H
        num = N // H + 1
        print(floor * 100 + num)