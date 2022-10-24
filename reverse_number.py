def reverse(number):
    rev_num = 0
    while number > 0:
        remainder = number % 10
        rev_num = (rev_num * 10) + remainder
        number = number // 10
    return  rev_num
number = int(input("Enter the number please: "))
print(reverse(number))
