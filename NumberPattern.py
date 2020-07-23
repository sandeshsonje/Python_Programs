def NumberPattern(n):
    
    for i in range(1,n+1):
        for j in range(1,n-i+1):
            print(' ',end='')
        x=i
        for j in range(1,i*2):
            print(x,end='')
            if j<i:       #i=4  j=[1,2,3,4,5,6,7]
                x=x-1     # x = 4,3,2,1
            else:         # 5<4 will go in else stmt and increment the values 
                x=x+1     # x = 1,2,3,4
        print()

def main():
    n = int(input('Enter rows = '))
    NumberPattern(n)

if __name__=='__main__':
    main()
