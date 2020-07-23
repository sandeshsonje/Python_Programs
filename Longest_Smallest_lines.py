def Longest_Smallest_Lines(filename): 
    fd = open(filename)
    line = fd.readline()
    max_lines = line
    min_lines = line

    while line != "":
        line = fd.readline()
        if line == '\n' or line == '':
            continue
        if len(line) > len(max_lines):
            max_lines = line
        elif len(line)< len(min_lines):
            min_lines = line
    return max_lines,min_lines
 
def main():
    max_lines,min_lines = Longest_Smallest_Lines(input("Enter filename = "))
    print("Maxline = {}\nMinline = {}".format(max_lines,min_lines))

if __name__=='__main__':
    main()
