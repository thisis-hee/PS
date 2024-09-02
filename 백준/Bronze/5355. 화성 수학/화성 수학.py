T=int(input())

for _ in range(T):
    calculate_list=list(input().split())
    calculate_list[0]=float(calculate_list[0])

    value=calculate_list[0]

    for i in range(1,len(calculate_list)):
        if(calculate_list[i]=='@'):
            value*=3
        elif(calculate_list[i]=='%'):
            value+=5
        elif(calculate_list[i]=='#'):
            value-=7

    print('%0.2f'%value)