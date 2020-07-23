def CountOneBits(n):
    count = 0
    while n!=0:
        count += 1
        n = n&(n-1)
    return count

def main():
    n = eval(input('Enter number = '))
    print(CountOneBits(n))
    
if __name__=='__main__':
    main()
    
