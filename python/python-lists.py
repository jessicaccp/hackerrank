# Lists
# By https://www.hackerrank.com/jessicaccp on Aug 5, 2023

if __name__ == '__main__':
    arr = []
    
    N = int(input())
    for _ in range(N):
        tmp = input().split()
        
        if tmp[0] == "insert":
            arr[int(tmp[1]):int(tmp[1])] = [int(tmp[2])]
        elif tmp[0] == "print":
            print(arr)
        elif tmp[0] == "remove":
            arr.remove(int(tmp[1]))
        elif tmp[0] == "append":
            arr.append(int(tmp[1]))
        elif tmp[0] == "sort":
            arr.sort()
        elif tmp[0] == "pop":
            arr.pop()
        elif tmp[0] == "reverse":
            arr = arr[::-1]