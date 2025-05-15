import sys
input=sys.stdin.readline

A,B,C,X,Y=map(int,input().split())

if(A+B<=2*C):
    print(A*X+B*Y)
else:
    sum=0
    sum+=min(X,Y)*2*C
    if(X>min(X,Y)):
        if(A>2*C):
            sum+=(X-min(X,Y))*2*C
        else:
            sum+=(X-min(X,Y))*A
        print(sum)
    elif(Y>min(X,Y)):
        if(B>2*C):
            sum+=(Y-min(X,Y))*2*C
        else:
            sum+=(Y-min(X,Y))*B
        print(sum)
    else:
        print(sum)
