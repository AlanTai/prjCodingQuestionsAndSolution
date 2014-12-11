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
                    
    return result_matrix
                    
    
    
if __name__ == "__main__":
    given_str = "XMJYAUZ;MZJAWXU"
    
    list_str = given_str.split(";")
    str1 = list_str[0]
    str2 = list_str[1]
    print difflib.SequenceMatcher(None, str1, str2).get_matching_blocks()
    print solution(given_str)
    # result_matrix = [[],[]]
#     result_matrix[0].append(0)
#     print result_matrix
    
    
    
    
    