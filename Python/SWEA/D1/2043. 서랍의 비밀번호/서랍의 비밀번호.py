P,K=map(int,input().split())

count=1
while(True):
    if(K==P):
        print(count)
        break
    elif(K!=P):
        K+=1
        count+=1
