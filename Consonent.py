def Consonent(string):
    count = 0
    for ch in string:
        if ch in 'aeiouAEIOU':
            continue
        count += 1
    return count

def main():
    x =input('Enter string = ')
    print(Consonent(x))

if __name__=='__main__':
    main()
    
        
    
