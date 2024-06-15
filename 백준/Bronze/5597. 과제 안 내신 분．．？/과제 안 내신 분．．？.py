# sort로 배열 정렬
arr=list(range(1,31))

for _ in range(28):
    submit=int(input())
    arr.remove(submit)

arr.sort()
print(arr[0])
print(arr[1])
