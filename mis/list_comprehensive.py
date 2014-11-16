given_list = [0, 1, 2, -1, 4, 12, 6, -7, 8, 9, 11, -11, 12, 13, 14, 15, 16, 17, 18, 19]
result_1 = filter(lambda x: x % 3 == 2, given_list)
print result_1

result_2 = [x for i, x in enumerate(given_list) if i % 3 == 2]
print result_2

x = "abcdefghijklm"
print [ith + jth for ith, jth in zip(x[::2], x[1::2])]