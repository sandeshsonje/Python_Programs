def pattern1(n):
    for i in range(1,n+1):
        for j in range(i):
            print(' ',end=' ')
        for j in range(1,n+1-i):
            print('*',end=' ')
        print()

def main():
    n = int(input('enter rows = '))
    pattern1(n)

if __name__=='__main__':
    main()
