#Using sorted()

books=[('Atlas Shrugged',1005),('Black Swan',2001),('Sapiens',999)]
print(sorted(books,key=lambda x:x[1]))

#User defined  function

def Sort_Tuple(books):  
    l = len(books)  
    for i in range(0,l):  
          for j in range(0, l-i-1):  
            if (books[j][1] > books[j + 1][1]):  
                temp = books[j]  
                books[j]= books[j + 1]  
                books[j + 1]= temp  
    print(books)  

Sort_Tuple(books)
