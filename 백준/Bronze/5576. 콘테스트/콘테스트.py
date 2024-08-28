W_list=[]
K_list=[]

for _ in range(10):
    W_list.append(int(input()))

for _ in range(10):
    K_list.append(int(input()))

W_list.sort(reverse=True)
K_list.sort(reverse=True)

print((W_list[0]+W_list[1]+W_list[2]),(K_list[0]+K_list[1]+K_list[2]))