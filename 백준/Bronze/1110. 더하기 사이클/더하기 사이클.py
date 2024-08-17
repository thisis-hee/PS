N=int(input())
count=0
if(N<10):
        a='0'+str(N)
else:
    a=str(N)

while(True):
    b=str(int(a[0])+int(a[1]))
    a=a[1]+b[len(b)-1]
    count+=1
    if(int(a)==N):
        break

print(count)