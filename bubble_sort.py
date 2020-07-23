def bubble_sort(l1):
    for i in range(len(l1)-1):
        for j in range(len(l1)-i-1):
            if l1[j]>l1[j+1]:
                temp = l1[j]
                l1[j]=l1[j+1]
                l1[j+1]=temp
    return bubble_sort
    

def main():
    l1 = eval(input('Enter list = '))
    print('the array sorted in ascending order is : ')
    print(bubble_sort(l1))

if __name__=='__main__':
    main()
