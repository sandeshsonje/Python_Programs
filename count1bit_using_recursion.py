def Count1BitRecursion(n):
    if n==0:
        return 0
    return 1 + Count1BitRecursion(n&(n-1))

def main():
    n = eval(input('Enter number = '))
    print(Count1BitRecursion(n))
    
if __name__=='__main__':
    main()
