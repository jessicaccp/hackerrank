# Find a string
# By https://www.hackerrank.com/jessicaccp on Aug 6, 2023

def count_substring(string, sub_string):
    count = 0
    
    for i in range(0, len(string) - len(sub_string) + 1):
        if string[i:i + len(sub_string)] == sub_string:
            count += 1
    
    return count

