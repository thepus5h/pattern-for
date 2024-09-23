n=int(input('enter the value'))
for i in range (1,n+1):
    for j in range (1,n+1,2):
        print(j, end='')
        if(i %2==1):
            print()    