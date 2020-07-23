#wap to accept filename from user and print all the words starting with small(t) or capital(T)
# and ending small(t) or capital(T)
import re
def match_alphabet(myfile):
    fd = open(myfile)
    data = fd.read()
    regex_obj = re.compile(r"\bT\w+e\b",re.IGNORECASE)
    for match in regex_obj.finditer(data):
        print(match)

def main():
    myfile = input("Enter filename = ")
    match_alphabet(myfile)

if __name__=='__main__':
    main()
