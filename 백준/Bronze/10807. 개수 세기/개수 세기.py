'''
len=int(input())
arr=list(map(int,input().split(' ')))
find_num=int(input())
count=0
for i in range(len):
    if(arr[i]==find_num):
        count+=1

print(count)
'''

# 모범 답안
len=int(input())
arr=list(map(int,input().split(' ')))
find_num=int(input())

# 배열.count()로 개수 세기
print(arr.count(find_num))
