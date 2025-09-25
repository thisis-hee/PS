def solution(nums):
    real_nums = set(nums)
    cnt=len(nums)//2
    answer=min(cnt, len(real_nums))
    return answer