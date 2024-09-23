n=int(input('Enter n value: '))
for i in range (2,n+1,2):
    print("{:3d}".format(i),end='')
    if(i%10==0):
        print()