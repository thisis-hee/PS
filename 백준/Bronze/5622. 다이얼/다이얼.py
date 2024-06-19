S=input()
sum=0

for i in S:
    if(ord(i)>=65 and ord(i)<=67): # ABC
        sum+=3
    elif(ord(i)>=68 and ord(i)<=70): # DEF
        sum+=4
    elif(ord(i)>=71 and ord(i)<=73): # GHI
        sum+=5
    elif(ord(i)>=74 and ord(i)<=76): # JKL
        sum+=6
    elif(ord(i)>=77 and ord(i)<=79): # MNO
        sum+=7
    elif(ord(i)>=80 and ord(i)<=83): # PQRS
        sum+=8
    elif(ord(i)>=84 and ord(i)<=86): # TUV
        sum+=9
    elif(ord(i)>=87 and ord(i)<=90): # WXYZ
        sum+=10
    
print(sum)