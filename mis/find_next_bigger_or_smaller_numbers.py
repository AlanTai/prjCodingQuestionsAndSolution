'''
Created on Oct 25, 2014

@author: alantai
'''

def find_next_bigger_number(arg_integer):
    int_list = [int(elem) for elem in str(arg_integer)]
    head_list = []
    end_list = []
    sorted_end_list = []
    for ith in range(len(int_list) - 2, -1, -1):
        head_list = int_list[:ith + 1]
        end_list = int_list[ith + 1:]
        
        # find integer greater than current picked integer
        bigger_int = []
        for elem in end_list:
            if elem > int_list[ith]:
                bigger_int.append(elem)
                
        #
        if len(bigger_int) > 0:
            switched_int = min(bigger_int)
            current_int = head_list[ith]
            del head_list[ith]
            head_list.append(switched_int)
            end_list.remove(switched_int)
            end_list.append(current_int)
            
            sorted_end_list = quick_sort_upscending(end_list)
            break
            
    # return result
    if len(sorted_end_list) <= 0:
        return []
    else:
        return head_list + sorted_end_list

def find_next_smaller_combination(arg_integer):
    int_list = [int(elem) for elem in str(arg_integer)]
    head_list = []
    end_list = []
    sorted_end_list =[]
    
    for ith in range(len(int_list) - 2, -1, -1):
        head_list = int_list[:ith + 1]
        end_list = int_list[ith + 1:]
        
        #
        smaller_int = []
        for elem in end_list:
            if elem < int_list[ith]:
                smaller_int.append(elem)
                
        #
        if len(smaller_int) > 0:
            switched_int_of_end_list = max(smaller_int)
            switched_int_of_head_list = head_list[ith]
            del head_list[ith]
            head_list.append(switched_int_of_end_list)
            end_list.remove(switched_int_of_end_list)
            end_list.append(switched_int_of_head_list)
            
            sorted_end_list = quick_sort_upscending(end_list)[::-1]
            break
        
    # return result
    if len(sorted_end_list) <= 0:
        return []
    else:
        return head_list + sorted_end_list

def quick_sort_upscending(arg_ary):
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
        
def calculate_optimal_arrangement():
    given_integer = 165432
    ascending_result = given_integer
    descending_result = given_integer
    
    # find max and min
    int_list = [int(elem) for elem in str(given_integer)]
    max_boundary = quick_sort_upscending(int_list)
    min_boundary = max_boundary[::-1]
    max_boundary = ''.join(str(elem) for elem in max_boundary)
    max_boundary = int(max_boundary)
    min_boundary = ''.join(str(elem) for elem in min_boundary)
    min_boundary = int(min_boundary)
    
    print "Next 5 bigger numbers:"
    for ith in range(0, 5, 1):
        if ascending_result == "":
            break
        else:
            ascending_result = int(ascending_result)
        if ascending_result == max_boundary:
            break
        
        ascending_result = ''.join(str(elem) for elem in find_next_bigger_number(ascending_result))
        print ascending_result

    print "Next 5 smaller numbers:"
    for ith in range(0, 5, 1):
        if descending_result == "":
            break
        else:
            descending_result = int(descending_result)
        if descending_result == min_boundary:
            break

        descending_result = ''.join(str(elem) for elem in find_next_smaller_combination(descending_result))
        print descending_result

if __name__ == "__main__":
    calculate_optimal_arrangement()
        