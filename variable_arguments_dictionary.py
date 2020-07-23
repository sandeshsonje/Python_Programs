def VariableArgsDictionary(a,b,*args,**kwargs):
    print(a,b)
    print(type(args),type(kwargs))
    for x in args:
        print(x)

    for x in kwargs:
        print(x,kwargs[x])

def main():
    VariableArgsDictionary(10,20,4,5,6,7,name='Sandesh',hobby='cricket')

if __name__=='__main__':
    main()
