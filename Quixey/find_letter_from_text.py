def solution(arg_str, arg_text):
    letter_dict = {}
    result = []
    for letter in arg_str:
        if letter not in letter_dict:
            letter_dict[letter] = 1
        else:
            letter_dict[letter] += 1
            
    for letter in arg_text:
        if letter in letter_dict:
            if letter_dict[letter] != 0:
                letter_dict[letter] -= 1
                result.append(letter)
                if letter_dict[letter] == 0:
                    letter_dict.pop(letter, None)
            
        if not letter_dict:
            return 'all letters found'
            
    if not letter_dict:
        return 'all letters found'
    else:
        return letter_dict

if __name__ == "__main__":
    given_str = "hello, allen"
    given_text = '''Some keyboard shortcuts require the user to press a single key or a sequence of keys one after the other. Other keyboard shortcuts require pressing and holding several keys simultaneously. Keyboard shortcuts may depend on the keyboard layout (localization)'''
    
    print solution(given_str ,given_text)
    