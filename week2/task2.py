def average(array):
    array = set(array)  
    average = sum(array) / len(array)  
    return format(average, ".3f")
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)