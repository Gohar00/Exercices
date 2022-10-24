def max(data):

    j = 0
    i = data[0]
    while j < len(data):
        if data[j] >= i:
            i = data[j]
        j += 1
    return i
print(max([-1, -5, -2, -1]))