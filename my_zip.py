def my_zip(*args):

    min_len = len(args[0])
    for i in args:
        if len(i) < min_len:
            min_len = len(i)

    tp = ()
    for el in range(min_len):
        for j in args:
            j = list(j)
            tp = tp + (j[el],)
        yield tp
        tp = ()