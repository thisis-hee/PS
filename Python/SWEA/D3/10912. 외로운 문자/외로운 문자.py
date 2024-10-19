T=int(input())

for i in range(1,T+1):
    word=list(input())
    word.sort()
    j=0
    while(True):
        try:
            if(word[j]!=word[j+1]):
                j+=1
            else:
                del word[j:j+2]
                j=0
        except:
            break
    
    if(word==[]):
        print(f'#{i} Good')
    else:
        print(f'#{i}',''.join(word))
    