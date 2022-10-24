
def check(lst):

    lst = lst.split(' ')
    i = 0
    new_lst = sorted(lst)
    print('list must be: ', new_lst)
    return lst == new_lst or lst == new_lst[::-1]

lst = input("Enter your list's number with space: ")
print(check(lst))
