
import sys
test_cases = open(sys.argv[1], 'r')
list_given_var = []
for test in test_cases:
    # ignore test if it is an empty line
    # 'test' represents the test case, do something with it
    list_given_var.append(test)

test_cases.close()

specified_number = list_given_var[0]
list_str = list_given_var[1:]

ith = 0
while ith < len(list_given_var):
    if ith == 0 or len(list_given_var[ith - 1]) >= len(list_given_var[ith]):
        ith += 1
    else:
        list_given_var[ith], list_given_var[ith - 1] = list_given_var[ith - 1], list_given_var[ith]
        ith -= 1
        
for jth in range(0, specified_number):
    print list_given_var[jth]
        