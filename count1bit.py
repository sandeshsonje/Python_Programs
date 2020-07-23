def count1bit(n):
    count = 0
#    if n!=0:
#        return 1 + count1bit(n&(n-1))
    if n == 0:
        return count
    count += 1
    n=n&(n-1)
    return count1bit(n)

def main():
    n = eval(input('Enter number = '))
    print(count1bit(n))

if __name__=='__main__':
    main()
    
