# check nos is odd or even without using arithmatic operator
def IsOdd(n):
    if((n & 1)== 0):
        return True
    else:
        return False

def main():
    n= int(input('Enter number = '))
    if(IsOdd(n)==False):
        print('Odd')
    else:
        print('Even')

if __name__=='__main__':
    main()
    
