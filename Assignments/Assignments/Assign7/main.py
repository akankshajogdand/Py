import AreaOfShapes 

def Input():
    a=input('Select the shape of which you want to calculate the area 1.Circle 2.Square 3.Rectangle')
    p=int(a)
    
    if(p==1):
     c=input('Enter the radius of the circle :')
     r=int(c)
     result=AreaOfShapes.Circle(r)
     print(result)
    
    elif(p==2):
     s=input('Enter the length of the square :')
     length=int(s)
     result=AreaOfShapes.Square(length)
     print(result)
    
    elif(p==3):
     l=input('Enter the length of the rectangle:')
     length=int(l)
     b=input('Enter the breadth of the rectangle:')
     breadth=int(b)
     result=AreaOfShapes.Rectangle(length,breadth)
     print(result)
    
    else:
     print('Invalid Choice')
Input()
for i in range(4):
     d=input('Do you want to continue 1.Yes 2.No')
     opt=int(d)
     if(opt==1):
      Input()
     else:
         break

