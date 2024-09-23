T=int(input())

for _ in range(T):
    stack=[]
    vps=list(str(input()))
    for element in vps:
        if(element=='('):
            stack.append(element)
        else:
            if(len(stack)==0):
                stack.append(element)
                break
            else:
                stack.pop()
    if(len(stack)!=0):
        print("NO")
    else:
        print("YES")
