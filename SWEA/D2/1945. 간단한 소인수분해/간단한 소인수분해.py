T=int(input())

for i in range(1,T+1):
    a=0
    b=0
    c=0
    d=0
    e=0
    N=int(input())
    while(True):
        if(N%2==0):
            a+=1
            N=N//2
            continue
        elif(N%3==0):
            b+=1
            N=N//3
            continue
        elif(N%5==0):
            c+=1
            N=N//5
            continue
        elif(N%7==0):
            d+=1
            N=N//7
            continue
        elif(N%11==0):
            e+=1
            N=N//11
            continue
        else:
            break
    print(f'#{i} {a} {b} {c} {d} {e}')