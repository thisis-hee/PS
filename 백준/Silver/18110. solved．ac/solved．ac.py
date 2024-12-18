import sys
input=sys.stdin.readline

def round_function(num):
    if num - int(num) >= 0.5:
        return int(num + 1)
    else:
        return int(num)


n = int(input())

if n == 0:
    print(0)
else:
    num_list = []
    for _ in range(n):
        num_list.append(int(input()))

    threshold = round_function(n * 0.15)

    num_list.sort()

    if(threshold>=1):
        final_list = num_list[threshold:-threshold]

        sum = 0
        for i in range(len(final_list)):
            sum += final_list[i]
        print(round_function(sum / len(final_list)))
    else:
        sum = 0
        for i in range(len(num_list)):
            sum += num_list[i]
        print(round_function(sum / len(num_list)))
