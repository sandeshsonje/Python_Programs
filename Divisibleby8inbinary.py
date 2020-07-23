def Divisibleby8(n):
    return(n&7)== 0

def main():
    n = eval(input('Enter no = '))
    print(Divisibleby8(n))

if __name__=='__main__':
    main()
