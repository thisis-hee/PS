def solution(nums):
    
    cnt=len(nums)//2
    new_nums=set(nums)
    print(len(new_nums))
    print(cnt)
    if(len(new_nums)<=cnt):
        answer=len(new_nums)
    else:
        answer=cnt
    return answer