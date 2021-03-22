a=input("How many numbers you want to enter")
p=int(a)
l1=[]

for p in range(0,p):
    b=input("Enter the number:")
    q=int(b)
    l1.append(q)
print(l1)
def Addition(l):
    res=0
    for i in range(0,len(l)-1):
        res=l[i]+l[i+1]
    print(res)

def Subtract(l):
    sub=0
    for i in range(0,len(l)-1):
        sub=l[i]-l[i+1]
    print(sub)

def Divide(l):
    div=0
    for i in range(0,len(l)-1):
        div=l[i]/l[i+1]
    print(div)

def Product(l):
    pro=0
    for i in range(0,len(l)-1):
        pro=l[i]*l[i+1]
    print(pro)

def Mod(l):
    mod=0
    for i in range(0,len(l)-1):
        mod=l[i]%l[i+1]
    print(mod)


c=input("Operation you want to perform: 1.Add 2.Subtract 3.Multiply 4.Divide 5.Power 6.Mod" )
r=int(c)
if(r==1):
    Addition(l1)
elif(r==2):
    Subtract(l1)
elif(r==3):
    Divide(l1)
elif(r==4):
    Product(l1)
elif(r==5):
    Mod(l1)


