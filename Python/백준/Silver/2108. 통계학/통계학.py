import sys
input=sys.stdin.readline

N=int(input())

num_list=[]

for _ in range(N):
    num_list.append(int(input()))

num_dict={}

for i in range(len(num_list)):
    if(num_list[i] not in num_dict):
        num_dict[num_list[i]]=1
    else:
        num_dict[num_list[i]]+=1

mode=max(num_dict.values())

mode_list=[]

for k in num_dict.keys():
    if(num_dict[k]==mode):
        mode_list.append(k)


print(int(round(sum(num_list)/len(num_list),0)))
print(sorted(num_list)[len(num_list)//2])
if(len(mode_list)==1):
    print(mode_list[0])
else:
    print(sorted(mode_list)[1])
print(max(num_list)-min(num_list))

