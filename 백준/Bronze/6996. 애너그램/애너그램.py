T=int(input())

for _ in range(T):
    A,B=input().split()
    list_A=sorted(list(A))
    list_B=sorted(list(B))
    
    if(list_A==list_B):
        print(f'{A} & {B} are anagrams.')
    else:
        print(f'{A} & {B} are NOT anagrams.')