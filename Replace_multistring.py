a = eval(input('Enter string'))
if len(a) >= 3:
    if a.endswith('ing'):
        print(a.replace('ing','ly'))
    else:
        a += 'ing'
        
print(a)
    
    
