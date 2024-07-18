# 아스키 코드 이용해서 풀기
S=input()

A=list(S)
new_list=[]

for i in range(len(A)):
    if(ord(A[i])>=65 and ord(A[i])<=77):
        new_list.append(chr(ord(A[i])+13))
    elif(ord(A[i])>=78 and ord(A[i])<=90):
        new_list.append(chr(ord(A[i])-13))
    elif(ord(A[i])>=97 and ord(A[i])<=109):
        new_list.append(chr(ord(A[i])+13))
    elif(ord(A[i])>=110 and ord(A[i])<=122):
        new_list.append(chr(ord(A[i])-13))
    else:
        new_list.append(A[i])

for i in range(len(new_list)):
    print(new_list[i], end='')
