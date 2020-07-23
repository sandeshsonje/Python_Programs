def dict_of_squares(n):
    result=dict()
    for x in range(1,n+1):
        result[x] = x*x
    return result

def main():
    n = eval(input('Enter number = '))
    y = dict_of_squares(n)
    print(y)

if __name__=='__main__':
    main()
    
