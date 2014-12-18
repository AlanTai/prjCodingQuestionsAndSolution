from random import randrange

def solution(arg_list):
    arg_list.sort()
    dd = float("inf")
    xx = 0
    yy = 0
    for ith in range(len(arg_list) - 1):
        x, y = arg_list[ith], arg_list[ith + 1]
        if x == y:
            continue
        d = abs(x - y)
        
        if d < dd:
            xx, yy, dd = x, y, d
            
    return (xx, yy)
    
if __name__ == "__main__":
    given_list = [randrange(10 * 10) for ith in range(100)]
    print solution(given_list)