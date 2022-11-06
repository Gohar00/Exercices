def my_filter(func, sequence):

    for i in range(len(sequence)):
        if func(sequence[i]):
            yield sequence[i]