'''իրականացնել map3(func, data1, data2, data3) ֆունկցիա, որը վերադարձնում է նոր լիստ, որի մեջ ներառված են
func-ի կանչի արդյունքները data1, data2 և data3-ի համապատասխան անդամների անդամների վրա,
օրինակ, եթե ունենք sum(a, b, c) ֆունկցիան, որը վերադարձնում է a, b և c թվերի գումարը,
map(sum, [1, 2, 3], [10, 20, 30], [100, 200, 300]) կվերադարձնի [111, 222, 333]'''
def map3(func, data1, data2, data3):
    ml = []
    tmp = []
    j = 0
    if len(data1) == len(data2) == len(data3):
        print(True)
        while j < len(data1):
            tmp.append(data1[j])
            tmp.append(data2[j])
            tmp.append(data3[j])
            a = func(tmp)
            ml.append(a)
            tmp.remove(data1[j])
            tmp.remove(data2[j])
            tmp.remove(data3[j])
            j += 1
        return ml
    else:
        return ('Data lengths are not equal')

print(map3(sum, [1, 2, 3], [10, 20, 30], [100, 200, 300]))
print(map3(max, [1, 2, 3], [10, 20, 30], [100, 200, 300]))