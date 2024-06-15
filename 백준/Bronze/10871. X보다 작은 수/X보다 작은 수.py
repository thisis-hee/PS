N,X=map(int,input().split(' '))
arr=list(map(int, input().split(' ')))
new_arr=list()
for i in range(N):
    if(arr[i]<X):
        new_arr.append(arr[i])
# 배열 앞에 * 붙이면 띄어쓰기로 구분해서 출력해줌    
print(*new_arr)
