T=int(input())

for _ in range(T):
    
    count=int(input())
    A_list=[]
    B_list=[]

    A_list=list(input().split())
    A_list.sort()

    B_list=list(input().split())
    B_list.sort()

    if(A_list==B_list):
        print("NOT CHEATER")
    else:
        print("CHEATER")