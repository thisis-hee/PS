day_dict={
    'SUN':7,
    'MON':6,
    'TUE':5,
    'WED':4,
    'THU':3,
    'FRI':2,
    'SAT':1
}

T=int(input())

for i in range(1,T+1):
    day=input()
    print(f'#{i} {day_dict[day]}')