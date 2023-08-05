# Find the Runner-Up Score!
# By https://www.hackerrank.com/jessicaccp on Aug 4, 2023

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    arr = list(set(arr))
    arr.sort()
    print(arr[-2])
