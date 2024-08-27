# 핵심은 Ax-B(x-1)>=V 방정식을 떠올리는 것. 무조건 낮에만 정상에 도달 가능하므로. 그리고 math.ceil을 통해 올림하기.

import math

A,B,V=map(int,input().split())

print(math.ceil((V-B)/(A-B)))
