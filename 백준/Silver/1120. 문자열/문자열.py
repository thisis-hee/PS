import sys
input = sys.stdin.readline

A,B=input().rstrip().split()
diff=len(B)-len(A)

# 차이 날 수 있는 최대
final_diff=50

# diff+1만큼 루프
for i in range(diff+1):
    diff_cnt=0
    for j in range(len(A)):
        if(A[j]!=B[i+j]):
            diff_cnt+=1
    final_diff=min(final_diff,diff_cnt)

print(final_diff)