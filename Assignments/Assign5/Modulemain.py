import Module

print('1.Check if the number is perfect square')
print('2.Check if the number is prime')
print('3.Calculate factorial')
opt=int(input('Which operation do you want to perform?'))

if(opt==1):
    a=int(input('Enter a number'))
    result=Module.PerfectSquare(a)
    print(result)
elif(opt==2):
    b=int(input('Enter a number'))
    result=Module.Prime(b)
    print(result)
elif(opt==3):
    c=int(input('Enter a number'))
    result=Module.Factorial(c)
    print(result)
else:
    print('Invalid choice')
