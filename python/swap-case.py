# sWAP cASE
# By https://www.hackerrank.com/jessicaccp on Aug 6, 2023

def swap_case(s):
    new_s = ""
    for letter in s:
        if letter.upper() == letter:
            new_s += letter.lower()
        elif letter.lower() == letter:
            new_s += letter.upper()
        else:
            new_s += letter
            
    return new_s

