if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    has=tuple(integer_list)
    hashed=(hash(has))
    print (hashed)