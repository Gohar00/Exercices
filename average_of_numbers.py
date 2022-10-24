def numbers_list():

    num_lst = []
    number = input("Please enter the number: ")
    num_lst.append(int(number))

    while number != '':
        number = input("Please enter the number: ")
        if number != '':
            num_lst.append(int(number))

    return average(num_lst)

def average(lst):

    av = sum(lst) / len(lst)
    return f'average is: {av}\nthe numbers who is < average: {[i for i in lst if i < av ]}\nthe numbers who equal are: {[i for i in lst if i == av ]} \
           \nthe numbers who > average are: {[i for i in lst if i > av]}'

print(numbers_list())