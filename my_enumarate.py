def my_enumerate(it, start=0):

    for el in it:
        start += 1
        yield (start, el)
