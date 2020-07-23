def count_char_dict(sentence):
    result=dict()
    for ch in sentence:
        if result.get(ch) != None:
            result[ch] += 1
        else:
            result[ch] = 1
    return result

def main():
    x ="India is my country"
    y = count_char_dict(x)
    print(y)

if __name__=='__main__':
    main()
