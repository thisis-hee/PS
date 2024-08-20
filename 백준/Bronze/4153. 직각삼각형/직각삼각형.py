while(True):

    length=list(map(int,input().split()))
    length.sort()

    if(length[0]==length[1]==length[2]==0):
        break

    if(length[2]**2==length[0]**2+length[1]**2):
        print('right')
    else:
        print('wrong')