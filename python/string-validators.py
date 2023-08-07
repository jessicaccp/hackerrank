# String Validators
# By https://www.hackerrank.com/jessicaccp on Aug 6, 2023

if __name__ == '__main__':
    s = input()
    output = [False, False, False, False, False]
    
    for letter in s:
        if letter.isalnum():
            output[0] = True
        if letter.isalpha():
            output[1] = True
        if letter.isdigit():
            output[2] = True
        if letter.islower():
            output[3] = True
        if letter.isupper():
            output[4] = True
            
        if output == [True, True, True, True, True]:
            break
        
    for item in output:
        print(item)
