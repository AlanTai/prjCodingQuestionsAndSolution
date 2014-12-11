from collections import OrderedDict

# In a given text, if there are two or more identical characters in sequence, delete the repetitions and leave only the first character.

def remove_duplicated_char_in_each_word(arg_txt):
    char_list = []
    result = ""
    for char in arg_txt:
        if char != " " and char not in char_list:
            char_list.append(char)
            result = result + char
        elif char == " ":
            result = result + char
            char_list = []
    return result
    

if __name__ == "__main__":
    ''' remove duplicated characters and only keep the first character'''
    
    given_str = "Shellless mollusk lives in wallless house in wellness. Aaaarrghh!"
    # print "".join(OrderedDict.fromkeys(given_str))
    
    print remove_duplicated_char_in_each_word(given_str)
    # answer: Shels molusk lives in wales house in welns. Aargh!