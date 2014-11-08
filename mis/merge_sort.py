def merge_sort(arg_list):
    mid = len(arg_list) // 2
    lft, rgt = arg_list[:mid], arg_list[mid:]
    if len(lft) > 1:
        lft = merge_sort(lft)
    if len(rgt) > 1:
        rgt = merge_sort(rgt)
        
    res = []
    while lft and rgt:
        if lft[-1] >= rgt[-1]:
            res.append(lft.pop())
        else:
            res.append(rgt.pop())
            
    res.reverse()
    return (lft or rgt) + res
    
if __name__ == "__main__":
    given_list = [2,0,4,-2,2,2,3,4,2,2,-5,-3,4,6,5,4,-3,-6,4-3,6]
    print merge_sort(given_list)