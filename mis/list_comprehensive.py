given_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
result_1 = filter(lambda x: x % 3 == 2, given_list)
print result_1

result_2 = [x for i, x in enumerate(given_list) if i % 3 == 2]
print result_2