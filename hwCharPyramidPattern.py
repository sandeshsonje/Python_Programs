def CharPattern(n):
    for i in range(1,n+1):
        for j in range(1,n-i+1):
            print(' ',end='')
        x=i
        for j in range(1,i*2):
            print(chr(x+64),end='')
            if j < i:
                x=x-1
            else:
                x=x+1
        
        print()

def main():
    n = int(input('enter rows = '))
    CharPattern(n)

if __name__=='__main__':
    main()
