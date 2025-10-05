from itertools import product

def solution(word):
    answer = 0
    
    word_list=['A','E','I','O','U']
    dictionary = []
    
    for i in range(1,6):
        for j in product(word_list, repeat=i):
            dictionary.append(''.join(j))
    
    dictionary.sort()
    
    answer = dictionary.index(word)+1
    
    return answer