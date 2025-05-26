import sys
input = sys.stdin.readline

N,M=map(int,input().split())
tree_list=list(map(int,input().split()))

start=1
end=max(tree_list)

while start<=end:
    mid=(start+end)//2
    total_length=0
    for tree in tree_list:
        if(tree>=mid):
            total_length+=tree-mid
    if(total_length>=M):
        start=mid+1
    else:
        end=mid-1

print(end)
