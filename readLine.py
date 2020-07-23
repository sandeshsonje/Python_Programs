# wap to accept file name from user and print it line by line

def readLine(filename):
    fd = open(filename)
    if fd!=None:
        line = fd.readline()
    while line !="":
        print(line)
        line = fd.readline()

def main():
    filename = input("Enter filename= ")
    readLine(filename)   # calling Function

if __name__=='__main__':
    main()
