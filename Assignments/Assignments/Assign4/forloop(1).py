n=int(input('How many numbers do you want to enter'))

a=[]
for i in range(n):
    b=int(input('Enter number'))
    a.append(b)
print(a)

add=a[0]
sub=a[0]
multiply=a[0]
div=a[0]
intdiv=a[0]
mod=a[0]
power=a[0]

for i in range(0,len(a)-1):
    add+=a[i+1]
    sub-=a[i+1]
    multiply*=a[i+1]
    div/=a[i+1]
    intdiv//=a[i+1]
    mod%=a[i+1]
    power**=a[i+1]
    
print("Addition:",add)
print("Subtraction:",sub)
print("Multiplication:",multiply)
print("Division:",div)
print("Integer Division:",intdiv)
print("Modulo:",mod)
print("Power:",power)
