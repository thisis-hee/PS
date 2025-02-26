import sys
input=sys.stdin.readline

R,C=map(int,input().split())

arr=[list(input().rstrip()) for _ in range(R)]
arr_t=list(zip(*arr))

total_list=[]

for line in arr:
    word_list=''.join(line).split('#')
    for word in word_list:
        if(len(word)>=2):
            total_list.append(word)

for line in arr_t:
    word_list=''.join(line).split('#')
    for word in word_list:
        if(len(word)>=2):
            total_list.append(word)

total_list.sort()
print(total_list[0])