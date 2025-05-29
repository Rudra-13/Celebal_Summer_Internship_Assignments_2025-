import string
def print_rangoli(n):
    # your code goes here
    alphabet = string.ascii_lowercase
    lines = []

    for i in range(n):
        left = alphabet[n-1:i:-1]
        center = alphabet[i]
        right = alphabet[i+1:n]
        row = '-'.join(left + center + right)
        lines.append(row.center(4*n - 3, '-'))

    print('\n'.join(lines[::-1] + lines[1:]))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)