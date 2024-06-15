N,X=map(int,input().split(' '))
arr=list(map(int, input().split(' ')))
new_arr=list()
for i in range(N):
    if(arr[i]<X):
        new_arr.append(arr[i])
    
print(*new_arr)