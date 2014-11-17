def find_factors_pairs(arg_num):
    return set(reduce(list.__add__, [[i, arg_num / i] for i in range(1, int(arg_num ** 0.5) + 1) if arg_num % i == 0]))
    
if __name__ == "__main__":
    print find_factors_pairs(4234)