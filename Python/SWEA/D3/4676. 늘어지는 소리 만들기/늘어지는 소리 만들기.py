T=int(input())

for i in range(1,T+1):
    word=list(input())
    H=int(input())
    location=list(map(int,input().split()))
    location.sort()
    hipen_count=0
    
    for j in range(len(location)):
        word.insert(location[j]+hipen_count,'-')
        hipen_count+=1
    print(f'#{i}',''.join(word))