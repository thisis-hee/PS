N,M=map(int,input().split())

word_list=set()

for _ in range(N):
    word_list.add(input())

count=0

for _ in range(M):
    if(input() in word_list):
        count+=1

print(count)