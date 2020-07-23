def isSorted(l1):
    i=0
    while i+1 < len(l1):
        if(l1[i] > l1[i+1]):
            return False
        i += 1
    return True

def main():
    l1 = eval(input('Enter list = '))
    print(isSorted(l1))

if __name__=='__main__':
    main()
    
