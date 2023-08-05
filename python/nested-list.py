# Nested Lists
# By https://www.hackerrank.com/jessicaccp on Aug 5, 2023

if __name__ == '__main__':
    records = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
        
    records = sorted(records, key=lambda k: (k[1], k[0].lower()))
    
    lowest = records[0][1]
    second = 0
    for record in records:
        if record[1] > lowest and second == 0:
            second = record[1]
            print(record[0])
        elif record[1] == second:
            print(record[0])
