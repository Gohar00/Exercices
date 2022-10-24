def div(n):
    return [i for i in range(1, n) if n % i == 0]

number = int(input("enter the number: "))
print(div(number))
