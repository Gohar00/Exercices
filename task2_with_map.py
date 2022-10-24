'''իրականացնել map2(func, data1, data2) ֆունկցիա, դրա օգնությամբ գրել ծրագիր, որը կտպի էկրանին նոր լիստ, որի i-րդ անդամը կլինի bases-ի i-րդ
անդամը exp-ի i-րդ անդամով աստիճան բարձրացրած, որտեղ base = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100], exp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]'''
def map2(func, data1, data2):
    ml = []
    j = 0
    if len(data1) == len(data2):
        while j < len(data1):
            a = pow(data1[j], data2[j])
            ml.append(a)
            j += 1
        return ml
    else:
        return ('Data lengths are not equal')
base = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
exp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(map2(pow, base, exp))