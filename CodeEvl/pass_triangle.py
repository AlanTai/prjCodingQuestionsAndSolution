if __name__ == "__main__":

    with open("/Users/alantai/Desktop/test.txt", "r") as fp:
        result_sum = 0
        current_index = 0
        for line in fp:
            # ignore test if it is an empty line
            # 'test' represents the test case, do something with it
            list_number = line.split(" ")
            if len(list_number) == 1:
                result_sum = int(list_number[0])
            else:
                first_number = int(list_number[current_index])
                second_number = int(list_number[current_index + 1])
                if first_number > second_number:
                    result_sum += first_number
                else:
                    result_sum += second_number
                    current_index += 1
                
                
        print result_sum
            
    test_list = ["1", "\n"]
    test_list.remove('\n')
    print test_list
        
