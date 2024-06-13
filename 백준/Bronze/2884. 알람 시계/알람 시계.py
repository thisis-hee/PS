h, m=map(int,input().split(' '))
if(h!=0 and m<45):
    print(str(h-1)+' '+str(m+15))
elif(h!=0 and m>=45):
    print(str(h)+' '+str(m-45))
elif(h==0 and m<45):
    print(str(23)+' '+str(m+15))
elif(h==0 and m>=45):
    print(str(h)+' '+str(m-45))