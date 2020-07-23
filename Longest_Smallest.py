def Longest_Largest_Lines(filename): 
    fd = open(filename)
    max_lines = fd.readline()
    length = len(line)

    while line != "":
        line = fd.readline()
        if length > len(line):
            print(max_lines)
        else:
            print(line)

def main():
    filename = input("Enter filename = ")
    Longest_Largest_Lines(filename)

if __name__=='__main__':
    main()
