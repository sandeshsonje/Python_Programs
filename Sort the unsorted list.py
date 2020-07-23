def Sortit(l1):
    n = len(l1)
    temp = 0
    for i in range(n-1):
        for j in range(i+1,n):
            if l1[i]>l1[j]:
                temp = l1[i]
                l1[i] = l1[j]
                l1[j]= temp
    return l1

def main():
    l1 = eval(input('Enter list = '))
    print(Sortit(l1))

if __name__=='__main__':
    main()
    
