tup = (1, 2, 3, 6, 4)
remainder = 0
j = len(tup) - 1
i = 1
while j >= 0:
    remainder += tup[j] * i
    j -= 1
    i *= 10
print(remainder)