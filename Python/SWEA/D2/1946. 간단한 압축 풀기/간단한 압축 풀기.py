
T=int(input())

for i in range(1,T+1):
    N=int(input())
    word_list=[]
    for _ in range(N):
        C,K=input().split()
        for _ in range(int(K)):
            word_list.append(C)
    
    print(f'#{i}')
    stack=[]
    for word in word_list:
        stack.append(word)
        if(len(stack)==10):
            print(''.join(stack))
            stack.clear()
    print(''.join(stack))