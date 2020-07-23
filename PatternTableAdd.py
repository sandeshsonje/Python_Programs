def PatternTableAdd(n):
    for i in range(1,n+1):
        k=i
        for j in range(1,i+2):
            print(k,end=' ')
            k += i
        print()

def main():
    PatternTableAdd(4)

if __name__=='__main__':
    main()
