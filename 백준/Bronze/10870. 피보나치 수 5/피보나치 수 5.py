n=int(input())

fib_list=[0,1]
if(n==0):
    print(0)
else:
    for i in range(2,n+1):
        fib_list.append(fib_list[i-2]+fib_list[i-1])

    print(fib_list[len(fib_list)-1])