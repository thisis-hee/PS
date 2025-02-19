def solution(arr):
    answer=[arr[0]]
    cnt=0
    for i in range(1,len(arr)):
        if(answer[cnt]==arr[i]):
            pass
        else:
            answer.append(arr[i])
            cnt+=1
    return answer