def remove_occurences(data,ele):
    while ele in data:
        data.remove(ele)
    
    

def main():
    data = eval(input('Enter list = '))
    ele = int(input('Enter element which to remove = '))
    remove_occurences(data,ele)
    print(data)
    
if __name__=='__main__':
    main()
