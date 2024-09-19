count=int(input())

day=map(int,input().split())

sorted_day=sorted(day,reverse=True)

final_day=[]

d=1
for i in sorted_day:
    final_day.append(d+i)
    d+=1

print(max(final_day)+1)