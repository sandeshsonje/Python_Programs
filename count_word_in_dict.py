def count_word_dict(sentence):
    result=dict()
    for word in sentence.split():
        if result.get(word) != None:
            result[word] += 1
        else:
            result[word] = 1
    return result

def main():
    x ="India is my India"
    y = count_word_dict(x)
    print(y)

if __name__=='__main__':
    main()
