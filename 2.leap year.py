n=float(input("enter the year:"))
if(n>0 and n.is_integer()):
    if(n%4==0 or n%400==0):
        print('a leap year')
    else:
        print("not a leap year")
else:
    print("not a valid input")
