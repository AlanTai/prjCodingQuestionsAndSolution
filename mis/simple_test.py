import cryptomath
def remove_even_numbers(list_of_nums):
    new_list = []
    for i, val in enumerate(list_of_nums):
        if val % 2 == 0:
            new_list.append(val)
    return new_list
    
def new_remove_even_numbers(list_of_nums):
    return filter(lambda x: x % 2 == 0, list_of_nums)
    
def map_test(list_of_nums):
    return map(lambda x, y: x + 5 + y, list_of_nums, list_of_nums)
    
def list_comprehensive(str_list):
    return [i + j for i, j in zip(x[::2], x[1::2])]
        
        
if __name__ == "__main__":
    foo = [1, 2, 4, 5, 9, 123]
    x = "abcdefghijklm"
    bar = map_test(foo)
    print bar
    print list_comprehensive(x)