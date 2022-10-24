def calculator(x, y, z):
    while True:


        try:
            if z == '+':
                return x + y
            elif z == '-':
                return x - y
            elif z == '*':
                return x * y
            elif z == '/':
                return x / y
        except:
            print('Error')

