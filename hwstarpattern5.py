def pattern5(n):
    for i in range(n):
        for j in range(n-i):
            print(' ',end='')
        for j in range((i*2)-1):
            print('*',end='')
        print()

    for i in range(n,0,-1):
        for j in range(n-i):
            print(' ',end='')
        for j in range((i*2)-1):
            print('*',end='')
        print()

def main():
    n = int(input('enter rows = '))
    pattern5(n)

if __name__=='__main__':
    main()
