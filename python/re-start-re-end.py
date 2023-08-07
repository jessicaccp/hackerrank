# Re.start() & Re.end()
# By https://www.hackerrank.com/jessicaccp on Aug 5, 2023

import re

def main():
    s = input()
    k = input()
    removed = 0
    
    for i in range(len(s) // len(k)):
        string = re.search(k, s)
        if string == None and i == 0:
            print((-1, -1))
            break
        elif string == None:
            break
        else:
            output = (string.start() + removed, string.end() - 1 + removed)
            print(output)
            removed += string.start() + 1
            s = s[string.start() + 1:]
        

main()
