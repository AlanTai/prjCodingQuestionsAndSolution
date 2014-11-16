def solution(arg_paired_list):
    return map(lambda pair: max(pair), arg_paired_list)
    
if __name__ == "__main__":
    matrix = [[2,3,1,5,8], [-2,3,9,1,1], [12,3,4,-1,-9], [1,2,3,4,5], [0,0,2,3,13]]
    
    print reduce(lambda row_1, row_2: solution(zip(row_1, row_2)), matrix)