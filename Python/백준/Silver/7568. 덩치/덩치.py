import sys
input=sys.stdin.readline

N=int(input())

weight=[]
height=[]
for _ in range(N):
    a,b=map(int,input().split())
    weight.append(a)
    height.append(b)

ans=[]
for i in range(N):
    count=1
    # [:] 붙여줘야 다른 객체가 됨. 안붙이면 같은 메모리를 참조해 del을 하면 weight, height에서도 지워짐
    compare_w=weight[:]
    compare_h=height[:]
    del compare_w[i]
    del compare_h[i]
    for j in range(N-1):
        if(compare_w[j]>weight[i] and compare_h[j]>height[i]):
            count+=1
    ans.append(count)

print(*ans)
