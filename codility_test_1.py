'''
Created on Oct 22, 2014

@author: alantai
'''

def find_next_bigger_number(A):
    # write your code in Python 2.7
    result = []
    P = 1
    while True:
        if P > len(A) - 1:
            break
        
        sub_ary_1 = A[:P:1]
        sub_ary_2 = A[P+1::1]
        sum_sub_ary_1 = 0
        sum_sub_ary_2 = 0
        
        if len(sub_ary_1) == 0:
            sum_sub_ary_1 = 0
        else:
            sum_sub_ary_1 = sum(sub_ary_1)
        
        if len(sub_ary_2) == 0:
            sum_sub_ary_2 = 0
        else:
            sum_sub_ary_2 = sum(sub_ary_2)
            
        if sum_sub_ary_1 == sum_sub_ary_2:
            result.append(P)
        P += 1
        
    if len(result) == 0:
        return -1
    else:
        return result

if __name__ == "__main__":
    given_ary = [-1,3,-4,5,1,-6,2,1]
    print find_next_bigger_number(given_ary)