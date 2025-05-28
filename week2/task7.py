# Enter your code here. Read input from STDIN. Print output to STDOUT
def error_code(n):
    for i in range(n):
         try:
             s,m =list(map(int,input().split()))
             divide = s//m 
     
             print (divide)
         except ZeroDivisionError as e:
            print ("Error Code:",e)
         
         except ValueError as e:
            print("Error Code:", e)
      
if __name__ == '__main__':
    n = int(input())
    error_code(n)
    