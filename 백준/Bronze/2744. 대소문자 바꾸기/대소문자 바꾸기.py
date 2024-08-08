S=input()
s=list(S)

for i in range(len(s)):
    if(s[i].isupper()==True):
        s[i]=s[i].lower()
    elif(s[i].islower()==True):
        s[i]=s[i].upper()

for i in range(len(s)):
    print(s[i],end='')