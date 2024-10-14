import math

T=int(input())

for i in range(1,T+1):
    com_dict={}
    word=list(str(input()))
    for j in range(len(word)):
        if(word[j] not in com_dict):
            com_dict[word[j]]=1
        else:
            com_dict[word[j]]+=1
    count=0
    answer=0
    for k in com_dict.values():
        if(k==2):
            answer+=1
            count+=1
    if(answer==2 and count==2):
        print(f'#{i} Yes')
    else:
        print(f'#{i} No')