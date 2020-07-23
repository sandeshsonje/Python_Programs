def CountZeroBits(x):
    count = 1
    while(x!=x**32):
        x = x << 1
    
    
        
    return count

def main():
    n = eval(input('Enter number = '))
    print(CountZeroBits(n))
    
if __name__=='__main__':
    main()
