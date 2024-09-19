A,B=map(int,input().split())

N=int(input())

Hz_list=[]

for _ in range(N):
    Hz_list.append(int(input()))

abs_list=[abs(A-B)-1]

for i in range(len(Hz_list)):
    abs_list.append(abs(B-Hz_list[i]))

print(min(abs_list)+1)