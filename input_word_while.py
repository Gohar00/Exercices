'''Գրել ծրագիր, որը օգտատիրոջից սպասում է մուտք՝ բառերի ցանկ, մինչև օգտագործողը թողնի մուտքագրման տողը դատարկ: 
Դրանից հետո օգտատիրոջ մուտքագրած բառերը պետք է ցուցադրվեն էկրանին, բայց առանց կրկնությունների՝ յուրաքանչյուրը մեկ անգամ։ 
Այս դեպքում բառերը պետք է ցուցադրվեն նույն հաջորդականությամբ, որով դրանք մուտքագրվել են ստեղնաշարից'''
def words(lst):
    new_lst = []
    for i in lst:
        if i not in new_lst:
            new_lst.append(i)
    return new_lst[:-1]

def lstt(w):
    while w != '':
        w = input('enter the word: ')
        ml.append(w)
    return words(ml)

ml = []
w = input('enter the word: ')
ml.append(w)
print(lstt(w))