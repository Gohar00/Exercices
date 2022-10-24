def leap_year(year):
    if(year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
        return True
    return False

def count_of_month(year, month):

        if leap_year(year):
            if month % 2 == 1:
                return f' 31 day'
            elif month == 2:
                return f' 29 day'
        else:
            if month % 2 == 0 and month != 2:
                return f' 30 day'
            elif month == 2:
                return f' 28 day'

year = int(input("Please enter the year: "))
month = int(input("PLease enter the month: "))
print(count_of_month(year, month))