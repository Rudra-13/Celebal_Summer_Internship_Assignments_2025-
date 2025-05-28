# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

def check_regex(n):
    for i in range(n):
        pattern = input()
        try:
            re.compile(pattern)
            print(True)
        except re.error:
            print(False)

if __name__ == '__main__':
    n = int(input())
    check_regex(n)