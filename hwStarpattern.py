def starpattern1(n):
    for i in range(1,n+1):
        for j in range(1,n-i+1):
            print('*',end=' ')
            
        print()

def main():
    n = int(input('Enter rows = '))
    starpattern1(n)

if __name__=='__main__':
    main()
