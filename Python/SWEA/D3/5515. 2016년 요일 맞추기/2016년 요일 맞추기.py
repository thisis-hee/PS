date_dict={
    1:31,
    2:29,
    3:31,
    4:30,
    5:31,
    6:30,
    7:31,
    8:31,
    9:30,
    10:31,
    11:30,
    12:31
}

day_dict={
    1:4,
    2:5,
    3:6,
    4:0,
    5:1,
    6:2,
    0:3
}

T=int(input())

for i in range(1,T+1):
    m,d=map(int,input().split())
    day_sum=0
    for j in range(1,m):
        day_sum+=date_dict[j]
    day_sum+=d
    print(f'#{i} {day_dict[day_sum%7]}')