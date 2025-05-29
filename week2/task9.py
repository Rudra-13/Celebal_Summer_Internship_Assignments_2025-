# Enter your code here. Read input from STDIN. Print output to STDOUT
def deleting_items(my_set, n):
    for i in range(n):
        command = input().split()
        if command[0] == "pop":
            try:
                my_set.remove(min(my_set)) 
            except KeyError:
                pass
        elif command[0] == "remove":
            try:
                my_set.remove(int(command[1]))
            except KeyError:
                pass
        elif command[0] == "discard":
            my_set.discard(int(command[1]))
    return sum(my_set)

if __name__ == '__main__':
    s = int(input())
    my_set = set(map(int, input().split()))
    n = int(input())
    result = deleting_items(my_set, n)
    print(result)
