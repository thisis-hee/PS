def solution(want, number, discount):
    answer = 0
    product_dict=dict()
    
    for i, j in zip(want,number):
        product_dict[i]=j
    
    product_dict=sorted(product_dict.items())
    
    
    for i in range(len(discount)-len(want)+1):
        check_dict=dict()
        check=discount[i:i+10]
        
        for j in check:
            if j not in check_dict.keys():
                check_dict[j]=1
            else:
                check_dict[j]+=1
        
        check_dict=sorted(check_dict.items())
        
        if product_dict == check_dict:
            answer+=1
    
    return answer