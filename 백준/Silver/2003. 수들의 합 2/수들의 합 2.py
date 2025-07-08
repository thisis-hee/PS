import sys

input = sys.stdin.readline

N, M = map(int, input().split())
num_list = list(map(int, input().split()))

cnt = 0
l = 0
r = 1

while True:
    if l > r or r > N: break

    total = sum(num_list[l:r])
    if total < M:
        r += 1
    elif total > M:
        l += 1
    else:
        cnt += 1
        r += 1

print(cnt)
