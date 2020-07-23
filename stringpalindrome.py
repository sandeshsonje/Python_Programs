def palindrome(str1):
    rev=str1[::-1]
    if(str1==rev):
        print("str is palindrome")
    else:
        print("str is not palindrome")
        
def main():
    str1=str(input("enter the str"))
    palindrome(str1)
if __name__=='__main__':
    main()
    

