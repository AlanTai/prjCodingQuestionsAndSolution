import difflib

def solution(arg_str):
    list_str = given_str.split(";")
    ref_list1 = list(list_str[0])
    ref_list2 = list(list_str[1])
    result_matrix = []
    result = []
    
    for index1, char1 in enumerate(ref_list1):
        result_matrix.append([])
        for index2, char2 in enumerate(ref_list2):
            if index1 == 0 and index2 == 0:
                if char1 == char2:
                    result_matrix[index1].append(1)
                else:
                    result_matrix[index1].append(0)
            elif index1 != 0 and index2 == 0:
                if char1 == char2:
                    result_matrix[index1].append(result_matrix[index1 - 1][index2] + 1)
                else:
                    result_matrix[index1].append(result_matrix[index1 - 1][index2])
            elif index1 == 0 and index2 != 0:
                if char1 == char2:
                    result_matrix[index1].append(result_matrix[index1][index2 - 1] + 1)
                else:
                    result_matrix[index1].append(result_matrix[index1][index2 - 1])
            elif index1 != 0 and index2 != 0:
                if char1 == char2:
                    result_matrix[index1].append(result_matrix[index1][index2 - 1] + 1)
                else:
                    max_val = max(result_matrix[index1][index2 - 1], result_matrix[index1 - 1][index2])
                    result_matrix[index1].append(max_val)
                    
    max_length = max(result_matrix[len(result_matrix) - 1])
    return result_matrix
                    
def trackback(arg_matrix):
    result = {}
    for elem in arg_matrix:
        max_val = max(elem)
        max_val_index = elem.index(max_val)
        if max_val not in result:
            result[max_val] = max_val_index
        else:
            if result[max_val] > max_val_index:
                result[max_val] = max_val_index
    return result
                    
    
    
if __name__ == "__main__":
    given_str = "XMJYAUZ;MZJAWXU"

    list_str = given_str.split(";")
    str1 = list_str[0]
    str2 = list_str[1]
    list2 = list(str2)
    
    result_matrix = solution(given_str)
    result_dict = trackback(result_matrix)
    print "".join(list2[result_dict[key]] for key in result_dict)
    
    # print difflib.SequenceMatcher(None, str1, str2).get_matching_blocks()
    
    
    
import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    # 'test' represents the test case, do something with it
    print test
    
test_cases.close()
    
    
    
    
    