total=1
s=[0]*10

for _ in range(3):
    total=total*int(input())

for i in list(str(total)):
    if(i=='0'):
        s[0]+=1
    elif(i=='1'):
        s[1]+=1
    elif(i=='2'):
        s[2]+=1
    elif(i=='3'):
        s[3]+=1
    elif(i=='4'):
        s[4]+=1
    elif(i=='5'):
        s[5]+=1
    elif(i=='6'):
        s[6]+=1
    elif(i=='7'):
        s[7]+=1
    elif(i=='8'):
        s[8]+=1
    elif(i=='9'):
        s[9]+=1

for i in range(len(s)):
    print(s[i])