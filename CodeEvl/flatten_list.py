'''
Created on Oct 26, 2014

@author: alantai
'''

def solution(A):
    result = []
    while len(A) > 0:
        if isinstance(A[0], list):
            result += solution(A[0])
        else:
            result.append(A[0])
        
        del A[0]    
    return result
        
        
if __name__ == "__main__":
    given_list = [1,2,[5,4,3,[2,1,[2,5,4,7,[0]]]],[0,1,[2]],5,[3,4,[1,2,9,0],[4,3,[3,[2,0,0,[1,2],1],2]]],2,[1,2,[4],5,4,[1,2,3]],1,2,9]
    print solution(given_list)