import math

def PerfectSquare(n):
    root=math.sqrt(n)
    if(n==root*root):
        print('The entered number is a perfect square')
    else:
         print('The entered number is not a perfect square')

def Prime(n):
        count=0
        i=2
        while(i<=n//2):
            if(n%i==0):
                count=count+1
        if(count==0):
             print('The entered number is prime')
        else:
            print('The entered number is not prime')

def Factorial(n):
    if(n==1):
        return n
    else:
        return n*Factorial(n-1)
