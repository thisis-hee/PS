A,B,C=map(int,input().split(' ')) # map을 통해 int형으로 한 번에 변환
print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)