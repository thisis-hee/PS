from collections import deque

def solution(n, words):
    answer = []
    
    check = []
    
    for i in range(len(words)):
        if not check:
            check.append(words[i])
        else:
            if check[-1][-1]!=words[i][0] or words[i] in check:
                answer.append(i%n+1)
                
                if (i+1)%n==0:
                    answer.append((i+1)//n)
                else:
                    answer.append((i+1)//n+1)
                
                break
            else:
                check.append(words[i])
    if len(check) == len(words):
        answer.append(0)
        answer.append(0)
    
    return answer