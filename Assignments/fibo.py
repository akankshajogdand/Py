k=int(input('Enter any no'))

if(k<1):
    print('Invalid Input')
else:
    z=0
    j=1
    c=z+j
    print(z)
    print(j)
    for i in range(k):
        while(c<=k):
            print(c)
            z=j
            j=c
            c=z+j
