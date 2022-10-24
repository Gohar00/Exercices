def div(n):
    return sum([i for i in range(1, n) if n % i == 0]) == n
number = int(input("Enter the number please: "))
print(div(number))