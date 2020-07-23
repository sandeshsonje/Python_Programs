def add(*args):
    print(type(args))
    print(args)
    result = 0
    for i in args:
        result += i
    return result

def main():
    print(add(1,2))
    print(add(100,200,300,400))

if __name__=='__main__':
    main()
