#In the Gregorian calendar, three conditions are used to identify leap years:
#The year can be evenly divided by 4, is a leap year, unless:
#The year can be evenly divided by 100, it is NOT a leap year, unless:
#The year is also evenly divisible by 400. Then it is a leap year.
#This means that in the Gregorian calendar, the years 2000 and 2400 are
# leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years. Source
def is_leap(year):
    leap = False
    print("Entrando al primer if", year % 4 )
    if year % 4 == 0:
        print("Entro al true del primer if, ")
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        return True
    else:
        print("Entrando al false del primer if")
        return False
print(is_leap(5))
