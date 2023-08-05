# Finding the percentage
# By https://www.hackerrank.com/jessicaccp on Aug 5, 2023

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    output = 0
    
    if student_marks[query_name]:
        for grade in student_marks[query_name]:
            output += float(grade)
        print("{:.2f}".format(output/3.0))
