def get_median(data):

    index = ((len(data) - 1) // 2)
    if len(data) % 2 == 1:
        return f'the median is: {data[index]}'
    return f'the median is {(data[index] + data[index + 1]) / 2}'

print(get_median([5, 2, 3, 8, 9, -2, 4]))
