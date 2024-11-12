import sys
input=sys.stdin.readline

while(True):
    string=input().rstrip()
    if(string=='.'):
        break
    else:
        stack=[]
        for i in range(len(string)):
            if(string[i]=='(' or string[i]=='['):
                stack.append(string[i])
            elif(string[i]==')'):
                stack.append(string[i])
                if(stack[len(stack)-2]=='('):
                    stack.pop()
                    stack.pop()
            elif(string[i]==']'):
                stack.append(string[i])
                if(stack[len(stack)-2]=='['):
                    stack.pop()
                    stack.pop()
        if stack:
            print('no')
        else:
            print('yes')


