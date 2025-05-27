def minion_game(string):
    # your code goes here
    vowels = "AEIOU"
    KEVIN = 0
    STUART = 0
    n = len(string)

    for i in range(n):
        if string[i] in vowels:
            KEVIN = KEVIN + (n - i)
        else:
            STUART =STUART +(n - i)

    if KEVIN > STUART:
        print("KEVIN", KEVIN)
    elif STUART > KEVIN:
        print("KEVIN", STUART)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)