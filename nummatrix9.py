n=int(input('Enter n value: '))
for i in range (1,n+1):
    print("{:3d}".format(i),end='')
    if(i%5==0):
        print()