def my_range(start=0, stop=0, step=1):

    lst = []
    if start < stop and step > 0:
        while start < stop:
            lst.append(start)
            start = start + step
    elif start > stop and step < 0:
        while start > stop:
            lst.append(start)
            start = start + step
    elif step == 0:
        raise ValueError("range() arg 3 must not be zero!")

    return lst