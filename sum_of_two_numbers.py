def sum_of_number(a, b):
    sum = 0
    while a <= b:
        sum += a
        a += 1
    return sum
print(sum_of_number(1, 3))