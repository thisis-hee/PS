# 띄어쓰기 없이 붙여서 출력하려면 sep 사용
T=int(input())
for _ in range(T):
    string=input()
    print(string[0],string[len(string)-1], sep='')
