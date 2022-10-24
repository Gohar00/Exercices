good = []
bad = []
for i in mydict.values():
    if i <= 6:
        bad.append(list(mydict.keys())[list(mydict.values()).index(i)])
    else:
        good.append(list(mydict.keys())[list(mydict.values()).index(i)])
print("bad students are: ",bad)
print("good students are: ",good)