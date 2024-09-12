string=list(input())

happy=0
sad=0

for i in range(len(string)-2):
    if(string[i]==':'):
        if(string[i+1]=='-' and string[i+2]=='('):
            sad+=1
        elif(string[i+1]=='-' and string[i+2]==')'):
            happy+=1

if(happy==sad==0):
    print('none')
elif(happy==sad):
    print('unsure')
elif(happy>sad):
    print('happy')
else:
    print('sad')