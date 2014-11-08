def gnome_sort(arg_list):
    ith = 0
    while ith < len(arg_list):
        if ith == 0 or arg_list[ith - 1] <= arg_list[ith]:
            ith += 1
        else:
            arg_list[ith], arg_list[ith - 1] = arg_list[ith - 1], arg_list[ith]
            ith -= 1
            
    return arg_list
    
if __name__ == "__main__":
    given_list = [12,2,5,4,4,5,4,6,4,56,-9,-4,2,6,8,8]
    print gnome_sort(given_list)