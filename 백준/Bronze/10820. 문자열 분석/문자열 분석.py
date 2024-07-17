# ord -> 아스키로 바꿔주는 함수
# try - except 문
while(True):
    try:
        String=input()
        lower=0
        upper=0
        number=0
        space=0
        for i in range(len(String)):
            if(ord(String[i])==32):
                space+=1
            elif(ord(String[i])>=65 and ord(String[i])<=90):
                upper+=1
            elif(ord(String[i])>=97 and ord(String[i])<=122):
                lower+=1
            elif(ord(String[i])>=48 and ord(String[i])<=57):
                number+=1
        print(lower, upper, number, space, end=' ')
        print()
    except EOFError:
        break
