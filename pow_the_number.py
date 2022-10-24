def pow(base, exp):
    res = 1
    count = 0
    if base == 0 and exp < 0:
        return "meaningless expression"
    elif exp < 0:
        while count < -exp:
            res = res * (1 / base)
            count += 1
    elif exp == 0:
        return res
    else:
        while count < exp:
            res = res * base
            count += 1

print(pow(2, 0))