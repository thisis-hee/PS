arr=[0]*10
for i in range(10):
    arr[i]=int(input())

remain_arr=[0]*10

for i in range(10):
    remain_arr[i]=arr[i]%42

print(len(set(remain_arr)))
