def  remove_all(data, val):

    j = 0
    new_list = []
    count = 0

    while j < len(data):
        if val != data[j]:
            new_list.append(data[j])
        j += 1

    return f"new-list: {new_list}"

data = [1, 7, 4, 3, 5, 7, 6, 7, 'a']
value = 7
print(remove_all(data, value))