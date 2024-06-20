a,b=map(int,input().split(' '))
c,d=map(int,input().split(' '))
e,f=map(int,input().split(' '))

x=[a,c,e]
y=[b,d,f]

if(x[0]==x[1]):
    g=x[2]
elif(x[1]==x[2]):
    g=x[0]
elif(x[0]==x[2]):
    g=x[1]

if(y[0]==y[1]):
    h=y[2]
elif(y[1]==y[2]):
    h=y[0]
elif(y[0]==y[2]):
    h=y[1]

print(g, h)