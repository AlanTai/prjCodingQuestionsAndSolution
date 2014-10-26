'''
Created on Oct 24, 2014

@author: alantai
'''
import random
def find_next_bigger_number(arg_list):
    sorted_list = quick_sort_upscending(arg_list)
    
    min_num = min(sorted_list)
    if min_num != 1:
        return "missing number is 1"
    max_num = max(sorted_list)
    if max_num != 10:
        return "missing number is 10"
    
    for ith in range(0, len(sorted_list) - 1, 1):
        if sorted_list[ith + 1] - sorted_list[ith] > 1:
            return "missing number is {0}".format((sorted_list[ith] + 1))

def quick_sort_upscending(arg_ary):
    smaller = []
    pivot_list = []
    bigger = []
    
    if len(arg_ary) <= 1:
        return arg_ary
    else:
        pivot_value = arg_ary[0]
        
        for ith in arg_ary:
            if ith < pivot_value:
                smaller.append(ith)
            elif ith > pivot_value:
                bigger.append(ith)
            else:
                pivot_list.append(ith)
                
    smaller = quick_sort_upscending(smaller)
    bigger = quick_sort_upscending(bigger)
    return smaller + pivot_list + bigger

if __name__ == "__main__":
    given_list = [1,2,3,4,5,6,7,8,9,10]
    
    # randomly delete one number
    rand = random.sample(given_list, 1)
    del given_list[rand[0] - 1]
    random.shuffle(given_list)
    print "original list: " + given_list.__str__()
    print find_next_bigger_number(given_list)