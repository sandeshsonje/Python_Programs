def pattern3(n):
    for i in range(1,n+1):
        for j in range(1,n-i+1):
            print(' ',end='')
        for j in range(1,i*2):
            print('*',end='')
        print()

def main():
    n = int(input('Enter rows= '))
    pattern3(n)             #calling function n

if __name__=='__main__':
    main()
