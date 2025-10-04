from itertools import permutations

def solution(numbers):
    answer=0
    all_num=set()
    numbers=list(numbers)
    
    for i in range(1,len(numbers)+1):
        for j in permutations(numbers, i):
            all_num.add(int(''.join(j)))
    
    if 0 in all_num:
        all_num.remove(0)
    if 1 in all_num:
        all_num.remove(1)
        
    for num in all_num:
        is_prime=True
        for i in range(2, int(num**(1/2))+1):
            if num%i==0:
                is_prime=False
                break
        if is_prime:
            answer+=1
    
    return answer