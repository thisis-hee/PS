T=int(input())

for _ in range(T):
    N = int(input())
    dict={}
    for _ in range(N):
        school, alcohol=input().split()
        dict[school]=int(alcohol)

    for i in dict.keys():
        if(dict[i]==max(dict.values())):
            print(i)
            break