from itertools import combinations

def solution(nums):
    answer = -1
    prime_cnt=0
    for i in combinations(nums, 3):
        check = sum(i)
        is_prime = True
        for j in range(2, int(check**(1/2))+1):
            if check%j == 0:
                is_prime = False
                break
                
        if is_prime:
            prime_cnt+=1

    return prime_cnt