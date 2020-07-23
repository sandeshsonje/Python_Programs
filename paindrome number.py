def ReverseNumber(n):
    rem = 0
    rev = 0
    while n!=0:
        rem = n%10
        rev = rev*10+rem
        n=int(n//10)
    return rev

def main():
    n = int(input("enter number = "))
    rev = ReverseNumber(n)
    if(n==rev):
        print('its palindrome')
    else:
        print('not palindrome')

if __name__ == '__main__':
    main()
