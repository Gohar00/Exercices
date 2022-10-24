def pop(data, i = None):

    val = data[-1]
    j = 0
    new_list = []
    if i == None:
        new_list = data[:-1]
    else:
        while j < len(data):
            if i == data[j]:
                val = i
                i = j
            j += 1
            new_list = data[:i] + data[i + 1:]

    return f"new-list: {new_list}  val: {val}"
data = [7, 1, 4, 3, 5, 6, 7, 'a']
print(pop(data, 2))
