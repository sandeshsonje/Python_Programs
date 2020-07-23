def push(l1,data):
    l1.append(data)
    
def pop(l1):
    return l1.pop()

def peep(l1):
   return l1[-1]

def isFull(l1):
    return len(l1)==10

def isEmpty(l1):
    return l1 == []

def main():
    l1 = eval(input('Enter list = '))
    
    

if __name__=='__main__':
    main()
