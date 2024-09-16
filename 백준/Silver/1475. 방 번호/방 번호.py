N=list(input())
set_count=0

num_dict={'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'0':0}

for i in range(len(N)):
    if(N[i]=='1'):
        num_dict['1']+=1
    elif(N[i]=='2'):
        num_dict['2']+=1
    elif(N[i]=='3'):
        num_dict['3']+=1
    elif(N[i]=='4'):
        num_dict['4']+=1
    elif(N[i]=='5'):
        num_dict['5']+=1
    elif(N[i]=='6'):
        num_dict['6']+=1
    elif(N[i]=='7'):
        num_dict['7']+=1
    elif(N[i]=='8'):
        num_dict['8']+=1
    elif(N[i]=='9'):
        num_dict['6']+=1
    elif(N[i]=='0'):
        num_dict['0']+=1

if(num_dict['6']%2==0):
    num_dict['6']=num_dict['6']//2
else:
    num_dict['6']=(num_dict['6']//2)+1


print(max(num_dict.values()))