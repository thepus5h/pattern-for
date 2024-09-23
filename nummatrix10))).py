n=int(input('Enter n value: '))
for i in range (1,n+1):
    for j in range(1,n+1):
       print("{:2d}".format(j),i,end='')
    print()    
        # print("{:3d}".format(i,j),end='')
    # if(i%5==0):
    #     print()