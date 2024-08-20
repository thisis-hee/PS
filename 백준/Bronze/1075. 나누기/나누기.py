# join 맨날 까먹음 ㅠ

N=int(input())
F=int(input())

new_num=list(str(N))
new_num[-1]='0'
new_num[-2]='0'
a=''.join(new_num)
a=int(a)

while(True):
    if(a%F==0):
        a=str(a)
        print(a[-2]+a[-1])
        break
    else:
        a+=1
