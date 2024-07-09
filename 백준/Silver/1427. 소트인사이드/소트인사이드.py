N=input()
list_int=list(map(int,list(N)))
list_int.sort(reverse=True)

for i in range(len(list_int)):
    print(list_int[i], end='')