import sys
import _ssl

def main():
    x=input("Enter the number for Fibonacci")
    for num in range(int(x)):
      print(fib(num))
    
def fib(a):
    if int(a)==0:
        return 0
    elif int(a)==1:
        return 1
    else:
        result=fib(a-1)+fib(a-2)
        return result
    
    

if 1==1:
  main()


    
 

