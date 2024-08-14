N=int(input())

s=list(map(int,input().split()))
s.sort()

sum=0
cum_sum=0
for i in range(len(s)):
    sum+=s[i]
    cum_sum+=sum

print(cum_sum)