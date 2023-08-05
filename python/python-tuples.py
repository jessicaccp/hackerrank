# Tuples
# By https://www.hackerrank.com/jessicaccp on Aug 5, 2023

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    
    t = tuple(integer_list)
    t = hash(t)
    
    print(t)
