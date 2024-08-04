# set 활용
N,M=map(int,input().split())
A=set(map(int,input().split()))
B=set(map(int,input().split()))

#print(A)
#print(B)
#print(A-B)
#print(B-A)
print(len(A-B)+len(B-A))
