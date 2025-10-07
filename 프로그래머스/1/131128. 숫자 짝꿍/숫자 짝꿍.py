from collections import Counter

def solution(X, Y):
    answer = ''
    
    X=Counter(X)
    Y=Counter(Y)
    check = []
    
    for x,y in X.items():
        if x in Y.keys():
            for i in range(min(y,Y[x])):
                check.append(x)
                
    if not check:
        answer='-1'
    else:
        if set(check)=={'0'}:
            answer='0'
        else:
            check.sort(reverse=True)
            answer=''.join(check)
    
    return answer