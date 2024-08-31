N,L=map(int,input().split())

heights=list(map(int,input().split()))
heights.sort()

i=0
while(True):
    if(L>=heights[i]):
        L+=1
        if(i==len(heights)-1):
            print(L)
            break
        i+=1
        
    else:
        print(L)
        break