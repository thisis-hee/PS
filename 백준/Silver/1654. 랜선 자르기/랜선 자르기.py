import sys

input = sys.stdin.readline

K, N = map(int, input().split())

lan_list = []

for _ in range(K):
    lan_list.append(int(input()))

lan_list.sort()

start = 1
end = lan_list[len(lan_list) - 1]
answer = 0

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for line in lan_list:
        cnt += line // mid

    if (cnt >= N):
        start = mid + 1
    else:
        end = mid - 1

print(end)