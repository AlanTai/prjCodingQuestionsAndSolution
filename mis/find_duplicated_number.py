import Queue

def solution(arg_list):
    dict_result = {}
    list_duplicated_numbers = []
    for elem in arg_list:
        if elem not in dict_result:
            dict_result[elem] = 1
        else:
            dict_result[elem] = dict_result[elem] + 1
            if elem not in list_duplicated_numbers:
                list_duplicated_numbers.append(elem)
            
    return list_duplicated_numbers
    
if __name__ == "__main__":
    given_list = [1,2,3,2,4,5,5,7,76,67,34,32,4,6,57,8,7,7,86,2,1,4,86]
    print solution(given_list)
    
    test_list = [1,2,3,4,5]
    q = Queue.Queue()
    while len(test_list) > 0:
        q.put( test_list.pop() )
    
    print q
    while q.qsize() > 0:
        print q.get()
        
        
        