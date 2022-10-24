'''Գլխավոր մրցանակը շահելու համար վիճակախաղի տոմսի վեց համարները պետք է համընկնեն խաղարկության ժամանակ պատահականության սկզբունքով
խաղարկված վեց թվերի հետ՝ 1-ից 49 միջակայքում: Գրեք ծրագիր, որը պատահականորեն կընտրի ձեր տոմսի համար վեց թիվ: Համոզվեք, որ այդ թվերի մեջ կրկնվող թվեր չկան:
Ցուցադրել տոմսի թվերը էկրանին աճման կարգով:'''

import random
def rand_numbers():
     lst = []
     for i in range(6):
         rand_num = random.randint(1, 49)
         lst.append(rand_num)
     return check_duplicate(lst)

def check_duplicate(lst):
    lst = sorted(lst)
    set_lst = set(lst)
    while len(lst) != len(set_lst):
        return rand_numbers()
    return f'your password is: {lst}'

print(rand_numbers())