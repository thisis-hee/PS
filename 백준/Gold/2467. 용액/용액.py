import sys

input = sys.stdin.readline

N=int(input())
num_list = list(map(int,input().split()))
num_list.sort()

left = 0
right = N-1
check_value = 100000000000000
answer=[0, 0]

while left < right:
    hap = num_list[left]+num_list[right]

    if abs(hap) < abs(check_value):
        check_value = hap
        answer=[num_list[left], num_list[right]]

    if hap>0:
        right-=1
    elif hap<0:
        left+=1
    else:
        break

print(*answer)
