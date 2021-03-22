a=input("Enter the first number")
p=int(a)
b=input("Enter the second number")
q=int(b)
c=input("Operation you want to perform: 1.Add 2.Subtract 3.Multiply 4.Divide 5.Power 6.Mod" )
r=int(c)
if(r==1):
    print("Sum :",(p+q))
   
elif(r==2):
    print("Difference :",(p-q))
    
elif(r==3):
    print("Product :",(p*q))
    
elif(r==4):
    print("Division :",(p/q))

elif(r==5):
    print("Power :",(p^q))

elif(r==6):
    print("Mod:",(p%q))




