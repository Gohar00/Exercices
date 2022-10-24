def is_symbols(sentence):

    symbols = ',.!@#$%^&*()?'
    mstr = sentence
    for i in mstr:
       if i in symbols:
           mstr = mstr.replace(i, '')
    return mstr

def is_palindrom(sentence):

    string = is_symbols(sentence)
    string = string.title()
    mstr = string.split(' ')
    rev_string = mstr[::-1]

    if mstr == rev_string:
        return "the string is palindrom"
    return "the string is not palindrom"

sentence = input("Enter your sentence: ")
print(is_palindrom(sentence))