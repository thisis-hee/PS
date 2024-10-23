T=int(input())

for i in range(1,T+1):
    a,b=input().split()
    word_list=input().split()
    print(f'#{i}')
    print('ZRO '*word_list.count('ZRO'),end='')
    print('ONE '*word_list.count('ONE'),end='')
    print('TWO '*word_list.count('TWO'),end='')
    print('THR '*word_list.count('THR'),end='')
    print('FOR '*word_list.count('FOR'),end='')
    print('FIV '*word_list.count('FIV'),end='')
    print('SIX '*word_list.count('SIX'),end='')
    print('SVN '*word_list.count('SVN'),end='')
    print('EGT '*word_list.count('EGT'),end='')
    print('NIN '*(word_list.count('NIN')-1),end='')
    print('NIN')
    