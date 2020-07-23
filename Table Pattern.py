def PatternDouble(n):
    for i in range(1,n+1):
        k=i
        for j in range(1,i+2):
            print(k,end=' ')
            k*=2
        print()

def main():
    n = eval(input('Enter no of rows = '))
    PatternDouble(n)

if __name__=='__main__':
    main()
