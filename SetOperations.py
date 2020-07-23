# wap to accept two list from user and find
# 1. Union
# 2. intersection
# 3. symmetric difference
# 4. isSubset
# 5. isDisjoint
# 6. isinstance

def Union(l1,l2):
    l3 = []
    for i in range(len(l1)):
        l3.append(l1[i])
    for i in range(len(l2)):
        if l2[i] not in l1:
            l3.append(l2[i])
    return l3

def intersection(l1,l2):
    l3 = []
    for i in range(len(l1)):
        if l1[i] in l2:
            l3.append(l1[i])
    return l3

def SymmetricDifference(l1,l2):
    l3 =[]
    for i in range(len(l1)):
        if l1[i] not in l2:
            l3.append(l1[i])
    for i in range(len(l2)):
        if l2[i] not in l1:
            l3.append(l2[i])
    return l3

def main():
    l1 = eval(input("Enter elements of first list = "))
    l2 = eval(input("Enter elements of second list = "))
    print('Union is = ',Union(l1,l2))
    print('Intersection is = ',intersection(l1,l2))
    print('SymmetricDifference is = ',SymmetricDifference(l1,l2))

if __name__=='__main__':
    main()
    
