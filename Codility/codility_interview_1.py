'''
Created on Oct 23, 2014

@author: alantai
'''

def solution_1(A):
    result = []
    P = 0
    
    while P < len(A) - 1:
        for ith in range(P + 1, len(A) , 1):
            if A[P] == A[ith]:
                result.append((P, ith))
        P += 1
                
    # return final answer
    if len(result) > 1000000000:
        return 1000000000
    else:
        return result
    
def solution_test_1(A):
    result = []
    P = 0
    
    while P < len(A) - 1:
        rest_len = (len(A) - 1 - P)
        
        # check if the rest of length is odd or even
        if (len(A) - 1 - P) % 2 == 0:
            half_rest_len = (len(A) - 1 - P) / 2
        else:
            half_rest_len = (len(A) - 1 - P) / 2 + 1
        
        # start calculating
        for ith in range(1, half_rest_len + 1 , 1):
            if  (rest_len - ith + 1 + P) != (P + ith) :
                if A[P] == A[(rest_len - ith + 1 + P)]:
                    result.append((P,(rest_len - ith + 1 + P)))
                    
            if A[P] == A[(P + ith)]:
                result.append((P, (P + ith)))
                
        # increase P by 1
        P += 1
                
    # return final answer
    if len(result) > 1000000000:
        return 1000000000
    else:
        return result
        

def solution_2(K, A):
    result = []
    P = 0
    
    while P < len(A):
        for ith in range(0, len(A) , 1):
            if (A[P] + A[ith]) == K:
                result.append((P, ith))
        P += 1
                
    # return final answer
    return result
    
def solution_test_2(K, A):
    result = []
    P = 0
    
    while P < len(A):
        #
        if len(A) % 2 == 0:
            half_len = len(A) / 2
        else:
            half_len = len(A) / 2 + 1
            
        for ith in range(0, half_len , 1):
            if ith != (len(A) - 1) - (ith):
                if (A[P] + A[(len(A) - 1) - (ith)]) == K:
                    result.append((P, (len(A) - 1) - (ith)))
                    
            if (A[P] + A[ith]) == K:
                result.append((P, ith))
        P += 1
                
    # return final answer
    return result
        
if __name__ == "__main__":
    ary_1 = [3,1,1,6,3,4,5,5,1,3,2,1,1,2,2,3,1,4]
    print "Q1. Ans.2 =========="
    print solution_1(ary_1)
    print "Q1. Ans.2 =========="
    print solution_test_1(ary_1)
    
    K = 6
    ary_2 = [1, 8, 3, 2 ,5 , 7, -2,-2,-1,-3,-1]
    print "Q2. Ans.1 =========="
    print solution_2(K, ary_2)
    print "Q2. Ans.2 =========="
    print solution_test_2(K, ary_2)
    
#     test_ary = [1,2,3]
#     print test_ary[-2]