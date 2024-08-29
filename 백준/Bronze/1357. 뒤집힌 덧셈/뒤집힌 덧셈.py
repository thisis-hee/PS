X,Y=map(int,input().split())

def Rev(x):
    x=list(str(x))
    x.reverse()
    new_x=''.join(x)
    return int(new_x)

print(Rev(Rev(X)+Rev(Y)))
