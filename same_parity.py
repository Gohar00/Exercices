def same_parity(n, *args):
    lst = []
    for i in args:
        if i % n == 0:
            lst.append(i)
    return lst

print(same_parity(3,21,34,45,45,78,6543,2322,234))