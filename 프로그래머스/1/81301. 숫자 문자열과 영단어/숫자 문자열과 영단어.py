num_dict={'zero':0,
         'one':1,
         'two':2,
         'three':3,
         'four':4,
         'five':5,
         'six':6,
         'seven':7,
         'eight':8,
         'nine':9}

def solution(s):
    result=[]
    new_word=[]
    for i in s:
        if(ord(i)>=48 and ord(i)<=57):
            result.append(str(i))
        else:
            new_word.append(i)
            if(''.join(new_word) in num_dict.keys()):
                result.append(str(num_dict[''.join(new_word)]))
                new_word=[]
    
    answer=int(''.join(result))
    return answer