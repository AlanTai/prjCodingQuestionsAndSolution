'''
Created on Oct 21, 2014

@author: alantai
'''

def is_prime(arg_number):
    prime_factors = set(reduce(list.__add__, ([i] for i in range(1, int(arg_number ** 0.5 ) + 1 ) if arg_number % i == 0 )))
    
    if len(prime_factors) == 1:
        return True
    else:
        return False
    
def is_palindrome(arg_number):
    digi_list = [int(x) for x in str(arg_number)]
    for jth in range(0, len(digi_list) / 2, 1):
        if digi_list[jth] != digi_list[ len(digi_list) - jth - 1]:
            return False
    return True
    
def find_prime_palindrome():
    ith = 10
    result = 0
    while True:
        if is_palindrome(ith):
            if is_prime(ith):
                result = ith
        ith += 1
        if ith > 1000:
            break
    return result

if __name__ == "__main__":
    print find_prime_palindrome()
    # print is_palindrome(929)
    # print is_prime(929)