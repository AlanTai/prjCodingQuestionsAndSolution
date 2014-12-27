'''
Created on Oct 26, 2014

@author: alantai
'''

# depth-first solution
def solution_dfs(A):
    result = []
    while len(A) > 0:
        if isinstance(A[0], list):
            result += solution_dfs(A[0])
        else:
            result.append(A[0])
        
        del A[0]    
    return result
    
# bread-first solution
def solution_bfs(arg_list):
    list_of_list = []
    
    while len(arg_list) > 0:
        elem = arg_list.pop()
        if isinstance(elem, list):
            list_of_list = list_of_list + elem
        else:
            yield elem
            
        if len(arg_list) == 0:
            arg_list = list_of_list
            list_of_list = []
        
        
if __name__ == "__main__":
    given_list = [1,2,[5,4,3,[2,1,[2,5,4,7,[0]]]],[0,1,[2]],5,[3,4,[1,2,9,0],[4,3,[3,[2,0,0,[1,2],1],2]]],2,[1,2,[4],5,4,[1,2,3]],1,2,9]
    print solution_dfs(given_list)
    
    given_list = [1,2,[5,4,3,[2,1,[2,5,4,7,[0]]]],[0,1,[2]],5,[3,4,[1,2,9,0],[4,3,[3,[2,0,0,[1,2],1],2]]],2,[1,2,[4],5,4,[1,2,3]],1,2,9]
    list_result = []
    for elem in solution_bfs(given_list):
        list_result.append(elem)
        
    print list_result
        
    
    
    
    