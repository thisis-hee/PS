import sys

input = sys.stdin.readline

N = int(input())
money_list = list(map(int, input().split()))
total = int(input())
if (sum(money_list) <= total):
    print(max(money_list))
else:
    start = 1
    end = max(money_list)

    while start <= end:
        mid = (start + end) // 2
        semi_total = 0
        for money in money_list:
            if (money <= mid):
                semi_total += money
            else:
                semi_total+=mid
        if(semi_total<=total):
            start=mid+1
        else:
            end=mid-1

    print(end)
