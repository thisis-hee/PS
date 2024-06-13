A,B,C=map(int,input().split(' '))

if(A==B==C):
    print(10000+A*1000)
elif(A==B!=C):
    print(1000+A*100)
elif(A==C!=B):
    print(1000+A*100)
elif(A!=B==C):
    print(1000+100*B)
elif(A!=B!=C):
    print(100*max(A,B,C))