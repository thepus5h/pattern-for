n=int(input('enter the value: '))
for i in range(1,n+1):
    print("{:2d} ".format(i), end='')
    if(i%5==0):
        print()
    
        