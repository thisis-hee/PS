import sys

input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().split()))
num_list.sort()

x = int(input())

start = 0
end = len(num_list) - 1
result = 0

while start < end:
    hap = num_list[start] + num_list[end]
    if hap == x:
        result += 1
        start += 1
        end -= 1
    elif hap < x:
        start+=1
    else:
        end-=1

print(result)
