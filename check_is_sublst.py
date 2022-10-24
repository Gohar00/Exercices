def is_sublist(l, s):

    is_sub = False
    if s == []:
        is_sub = True
    elif s == l:
        is_sub = True
    elif len(s) > len(l):
        is_sub = False

    else:
        for i in range(len(l)):
            if l[i] == s[0]:
                n = 1
                while (n < len(s)) and (l[i + n] == s[n]):
                    n += 1

                if n == len(s):
                    is_sub = True

    return is_sub


larger = [21, 34, 67, 34]
smaller = []
print(is_sublist(larger, smaller))