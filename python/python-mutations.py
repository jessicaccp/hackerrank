# Mutations
# By https://www.hackerrank.com/jessicaccp on Aug 6, 2023

def mutate_string(string, position, character):
    string = string[:position] + character + string[position + 1:]
    return string

