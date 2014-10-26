'''
Created on Oct 23, 2014

@author: alantai
'''
def solution_1(A):
    P = len(A)
    Q = len(A[0])
    result = []
    
    for ith in range(0, P, 1):
        for jth in range(0, Q, 1):
            
            sum_up = 0
            sum_bottom = 0
            sum_left = 0
            sum_right = 0
            
            # calculate sum of each region
            # up region
            if ith == 0:
                sum_up = 0
            else:
                for up_ith in range(0, ith, 1):
                    for column in range(0, Q, 1):
                        sum_up += A[up_ith][column]
                
            # bottom region
            if ith == P - 1:
                sum_bottom = 0
            else:
                for bottom_ith in range(ith + 1, P, 1):
                    for column in range(0, Q, 1):
                        sum_bottom += A[bottom_ith][column]
                
            # left region
            if jth == 0:
                sum_left = 0
            else:
                for left_jth in range(0, jth, 1):
                    for row in range(0, P, 1):
                        sum_left += A[row][left_jth]
                
            # right region
            if jth == Q - 1:
                sum_right = 0
            else:
                for right_jth in range(jth + 1, Q, 1):
                    for row in range(0, P, 1):
                        sum_right += A[row][right_jth]
            # evaluate
            if sum_up == sum_bottom and sum_left == sum_right:
                result.append((P,Q))
    return len(result)

def solution_2(A):
    sorted_list = quick_sort_upscending(A)
    result = []
    max_length = 0
    for ith in range(0, len(sorted_list), 1):
        subsequence = []
        subsequence.append(sorted_list[ith])
        for jth in range(ith + 1, len(sorted_list), 1):
            if sorted_list[jth] - sorted_list[ith] <= 1:
                subsequence.append(sorted_list[jth])
            else:
                break
        length_subsequence = len(subsequence)
        if length_subsequence > 1 and length_subsequence > max_length :
            max_length = length_subsequence
        # if length of rest list is smaller than the max length
        if (len(sorted_list) - 1) - (ith + 1) + 1 < max_length:
            break
            
        result.append(subsequence)
    return max_length
#     return result



def quick_sort_upscending( arg_ary):
    #init arrays
    smaller = []
    pivotList = []
    bigger = []
    
    #start algorithm
    if len(arg_ary) <= 1:
        return arg_ary
    else:
        pivot = arg_ary[0] #pick up first element as the pivot
        for i in arg_ary:
            if i < pivot:
                smaller.append(i)
            elif i > pivot:
                bigger.append(i)
            else:
                pivotList.append(i)
                
        #recursive sorting for sub arrays
        smaller = quick_sort_upscending(smaller)
        bigger = quick_sort_upscending(bigger)
        return smaller + pivotList + bigger

if __name__ == "__main__":
    test_maxtrix = [[2, 7, 5], [3, 1, 1]]
    print solution_1(test_maxtrix)

    print solution_2([6, 10, 1,0,2,3,2,1,2,2,3,3,2,4,5,2,3,3,67,7])