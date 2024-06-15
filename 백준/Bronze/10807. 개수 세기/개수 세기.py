len=int(input())
arr=list(map(int,input().split(' ')))
find_num=int(input())
count=0
for i in range(len):
    if(arr[i]==find_num):
        count+=1

print(count)