import sys
input=sys.stdin.readline

R,C=map(int,input().split())
arr=[list(input().rstrip()) for _ in range(R)]
v=[[0]*C for _ in range(R)]

for i in range(R):
    for j in range(C):
        if(arr[i][j]=='X'):
            v[i][j]=1

for i in range(R):
    for j in range(C):
        if(arr[i][j]=='X'):
            dir_cnt=0
            cnt=0
            for di, dj in ((-1,0),(1,0),(0,1),(0,-1)):
                ni,nj=i+di,j+dj
                if(0<=ni<R and 0<=nj<C):
                    dir_cnt+=1
                    if(arr[ni][nj]=='.'):
                        cnt+=1
            cnt+=4-dir_cnt
            if(cnt>=3):
                v[i][j]=0
'''
index_list=[]
for i in range(len(v)):
    for j in range(len(v[i])):
        if(v[i][j]==1):
            index_list.append((i,j))

print(v)
print(index_list)
'''
while True:
    if(sum(v[0])==0):
        v=v[1:]
        continue

    if(sum(v[len(v)-1])==0):
        v=v[:len(v)-1]
        continue
    
    sum_forward=0
    for i in range(len(v)):
        sum_forward+=v[i][0]
    
    if(sum_forward==0):
        for j in range(len(v)):
            v[j]=v[j][1:]

    sum_backward = 0
    for k in range(len(v)):
        sum_backward += v[k][len(v[k])-1]

    if (sum_backward == 0):
        for l in range(len(v)):
            v[l] = v[l][0:len(v[l])-1]


    if(sum_forward>0 and sum_backward>0):
        break

answer=[[0]*len(v[0]) for _ in range(len(v))]
for i in range(len(v)):
    for j in range(len(v[i])):
        if(v[i][j]==0):
            answer[i][j]='.'
        elif(v[i][j]==1):
            answer[i][j]='X'

for i in answer:
    print(''.join(i))
