
def find_max_vals_of_list(arg_paired_lists):
    return map(lambda pair: max(pair), arg_paired_lists)

if __name__ == "__main__":
    a = [1,2,7,4]
    b = [3,4,5,6]
    maxtrix = [[1,2,3,4], [3,2,1,4], [7,8,2,1]]
    
    print find_max_vals_of_list(zip(a, b))
    print reduce(lambda a, b: find_max_vals_of_list(zip(a,b)), maxtrix)
    