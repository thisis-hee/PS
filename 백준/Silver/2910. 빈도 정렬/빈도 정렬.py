import sys

input = sys.stdin.readline

X, Y = map(int,input().split())

num_list = list(map(int,input().split()))

num_dict=dict()

for num in num_list:
    if num not in num_dict.keys():
        num_dict[num]=1
    else:
        num_dict[num]+=1

dic = sorted(num_dict.items(), key=lambda x: x[1], reverse=True)
answer=[]
for i in dic:
    for j in range(i[1]):
        answer.append(i[0])

print(*answer)