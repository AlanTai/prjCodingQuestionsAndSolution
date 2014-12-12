import re
if __name__ == "__main__":
    result = ""
    line ="Cats are! - smarter, than dogs."
    to_upper_case = True
    for char in line:
        match_obj = re.match(r'[\w]', char)
        if match_obj:
            if to_upper_case:
                to_upper_case = False
                result += char.upper()
            else:
                to_upper_case = True
                result += char.lower()
        else:
            result += char
        
    print result