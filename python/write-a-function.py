# Write a function
# By https://www.hackerrank.com/jessicaccp on Aug 4, 2023

def is_leap(year):
    leap = False
    
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
        else:
            leap = True
                
    
    return leap

