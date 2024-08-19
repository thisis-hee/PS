def func(start):
    if(len(num)==6):
        print(' '.join(map(str,num)))
        
    else:
        for i in range(start,len(s)):
            if s[i] not in num:
                num.append(s[i])
                func(i+1)
                num.pop()


while(True):
    s=list(map(int,input().split()))
    if(s[0]==0):
        break
    else:
        num=[]
        func(1)
        print()