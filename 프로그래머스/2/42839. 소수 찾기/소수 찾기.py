from itertools import permutations

def solution(numbers):
    prime=[]
    num_list=[]
    for i in range(1,len(numbers)+1):
        for j in permutations(list(numbers),i):
            num_list.append(int(''.join(j)))
    num_list=set(num_list)
    num_list=sorted(num_list)
    
    num_list=[x for x in num_list if x not in (0,1)]
    print(num_list)
    for num in num_list:
        for i in range(2, int(num ** 0.5) + 1):
            if (num % i == 0):
                break
        else:
            prime.append(i)


    answer = len(prime)
    return answer