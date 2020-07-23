def fibonacci45(n):
    a=0
    b=1
    print(a,b,end=' ')
    for i in range(n-2):
        c = a+b
        a=b
        b=c
        if c < 45:
            print(c,end=' ')
    else:
        print('not exceed more than 45')

n = int(input('Enter number = '))


if __name__=='__main__':
    fibonacci45(n)
