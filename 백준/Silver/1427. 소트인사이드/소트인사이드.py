N=input()
# 문자열 하나하나 리스트에 넣는 법 그냥 list(N) 하면 됨
list_int=list(map(int,list(N)))

# sort 역순 정렬 = reverse
list_int.sort(reverse=True)

for i in range(len(list_int)):
    print(list_int[i], end='')
