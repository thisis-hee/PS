import sys
input=sys.stdin.readline

N,X=map(int,input().split())

num_list=list(map(int,input().split()))

new_list=[]
for i in range(len(num_list)):
    if(num_list[i]<X):
        new_list.append(num_list[i])

print(*new_list)