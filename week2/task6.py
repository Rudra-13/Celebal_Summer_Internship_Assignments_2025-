# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

def shoe_shop(x, size, n):
    stock = Counter(size)      
    total = 0                
     
    for i in range(n):          
        s, money = map(int, input().split()) 
        if stock[s] > 0:      
            total = total + money      
            stock[s] =  stock[s] - 1       
    return total                
if __name__ == '__main__':
    x=int(input())
    size=list(map(int,input().split()))
    n=int (input())
    result = shoe_shop(x,size,n)
    print(result)