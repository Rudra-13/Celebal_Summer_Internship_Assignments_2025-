# Enter your code here. Read input from STDIN. Print output to STDOUT
# s = input("Enter the string of digits: ")
# count = 1
# for i in range(1, len(s)):
#     if s[i] == s[i - 1]:
#         count = count + 1
#     else:
#         print(f"({count}, {s[i - 1]})", end=' ')
#         count = 1
# print(f"({count}, {s[-1]})")
# import sys

# if len(sys.argv) < 2:
#     print("Usage: python task3.py <string_of_digits>")
#     sys.exit()

# s = sys.argv[1]
# count = 1
# for i in range(1, len(s)):
#     if s[i] == s[i - 1]:
#         count += 1
#     else:
#         print(f"({count}, {s[i - 1]})", end=' ')
#         count = 1
# print(f"({count}, {s[-1]})")
s = input("Enter a string: ")

if not s:
    print("No input provided.")
else:
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            print(f"({count}, {s[i - 1]})", end=' ')
            count = 1
    print(f"({count}, {s[-1]})")
