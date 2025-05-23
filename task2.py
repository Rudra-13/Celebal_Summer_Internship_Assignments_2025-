def calculate(a,b):
    return(a+b),(a-b),(a*b)
    
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    sum,subtract,multiply=calculate(a,b)
    print(sum)
    print(subtract)
    print(multiply)