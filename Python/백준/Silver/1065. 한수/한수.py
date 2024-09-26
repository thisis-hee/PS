N=int(input())

if(N<=99):
    print(N)
else:
    count=0
    for i in range(100,N+1):
        diff=set()
        for j in range(len(str(i))-1):
            diff.add(int(str(i)[j+1])-int(str(i)[j]))
        if(len(diff)==1):
            count+=1
    print(count+99)