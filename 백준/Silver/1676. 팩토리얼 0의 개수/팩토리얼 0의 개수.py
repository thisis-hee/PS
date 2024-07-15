N=int(input())
factorial=1

# 팩토리얼 구하기
for i in range(1,N+1):
    factorial*=i

# 숫자 나누기
zero_list=list(str(factorial))

# 0 개수 세기
count=0
for j in range(len(zero_list)-1,-1,-1):
    if(zero_list[j]=='0'):
        count+=1
        continue
    else:
        break

print(count)