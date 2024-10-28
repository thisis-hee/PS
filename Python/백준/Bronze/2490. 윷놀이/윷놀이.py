for _ in range(3):
    num_list = input().split()
    if (''.join(num_list).count('0') == 0):
        print('E')
    elif (''.join(num_list).count('0') == 1):
        print('A')
    elif (''.join(num_list).count('0') == 2):
        print('B')
    elif (''.join(num_list).count('0') == 3):
        print('C')
    elif (''.join(num_list).count('0') == 4):
        print('D')
