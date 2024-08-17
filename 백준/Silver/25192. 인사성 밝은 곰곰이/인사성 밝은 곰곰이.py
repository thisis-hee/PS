N=int(input())
cnt=0
name_list=set()

for _ in range(N):
    name=input()
    if(name=='ENTER'):
        name_list.clear()
    else:
        if(name not in name_list):
            name_list.add(name)
            cnt+=1

print(cnt)