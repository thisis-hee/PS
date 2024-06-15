N=int(input())
arr=list(map(int,input().split(' ')))
max=max(arr)

# max(arr)을 바로 계산식에 넣으면 오류 남
for i in range(N):
    arr[i]=arr[i]/max*100

print(sum(arr)/len(arr))
