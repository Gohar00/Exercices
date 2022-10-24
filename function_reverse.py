def reverse(data):

    new_list = []
    j = len(data) - 1
    while j >= 0:
        new_list.append(data[j])
        j -= 1
    return new_list
print(reverse([1, 2, 34, 5, 7]))