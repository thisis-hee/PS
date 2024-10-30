N,game=input().split()

name=[]
for i in range(int(N)):
    name.append(input())

name=set(name)

if(game=='Y'):
    print(len(name))
elif(game=='F'):
    print(len(name)//2)
else:
    print(len(name)//3)