class Invalidinput(Exception):
    pass
try :
    a = float(input("Enter the number"))
    if a<0.1:
        raise Invalidinput
    print(a)
except Invalidinput:
    print("Invalid Input")
except ValueError:
    print("Enter correct input")


