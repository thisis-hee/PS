T=int(input())

for i in range(T):
    a=list(input().split())
    print(f'Case #{i+1}: ',end='')
    for j in range(len(a)):
        print(a.pop(),end=' ')