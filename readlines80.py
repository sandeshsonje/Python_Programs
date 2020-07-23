def readlines80(filename):
    fd = open(filename)
    line_nos = 1
    line_numbers = []
    line = fd.readline()
    while line != "":
            if len(line)<= 30:
                print(line)
            else:
                line_numbers.append(line_nos)
            line_nos += 1
            line = fd.readline()
    print("Line numbers of lines having more than 80 chars are ",line_numbers)

def main():
    filename = input("Enter filename = ")
    readlines80(filename)

if __name__=='__main__':
    main()
