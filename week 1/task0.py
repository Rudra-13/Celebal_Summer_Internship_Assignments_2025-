def print_formatted(number):
    # your code goes here
    width = len(bin(number)[2:])  

    for i in range(1, number + 1):
        dec = str(i).rjust(width)
        octal = format(i, 'o').rjust(width)
        hexa = format(i, 'X').rjust(width)
        binary = format(i, 'b').rjust(width)
        print(f"{dec} {octal} {hexa} {binary}")

if __name__ == '__main__':
    n = int(input())