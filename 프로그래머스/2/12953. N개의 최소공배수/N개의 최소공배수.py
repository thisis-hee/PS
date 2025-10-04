import math

def solution(arr):
    answer = 0
    gcd = []
    
    while len(arr)!=1:
        for i in range(len(arr)-1):
            gcd.append(int(arr[i]*arr[i+1]/math.gcd(arr[i],arr[i+1])))
        
        arr=gcd
        gcd=[]
    
    answer=arr[0]
    
    return answer