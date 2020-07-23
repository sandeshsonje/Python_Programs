def prime(n):
    if(n%2==0):
        return 0
    else:
        for x in range(3,n//2,2):
            if(n%x==0):
                return 0

def main():
    n = int(input('Enter no.'))
    if(prime(n)==0):
        print('it is not prime')
    else:
        print('it is prime')

if __name__=='__main__':
    main()
