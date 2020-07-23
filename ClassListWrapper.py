class ListWrapper:
    def __init__(self):
        self.list=[1,2,3,4,5,6,7]
    def __getitem__(self,obj):
        print(obj.start)
        print(obj.stop)
        print(obj.step)
        return self.list[obj.start:obj.stop:obj.step]

def main():
    x = ListWrapper()
    print(x[1:7:2])

if __name__=='__main__':
    main()
    
