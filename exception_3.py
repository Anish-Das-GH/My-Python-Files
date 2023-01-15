class Castvote(Exception):
    pass
class Cantvote(Exception):
    pass
try:
    name = str(input("Enter Name : "))
    age = int(input("Enter the age of "+name+" : "))
    if age >= 18:
        raise Castvote
    else:
        raise Cantvote
except ValueError:
    print("Invalid Value")
except Castvote :
    print("User can cast vote")
except Cantvote:
    print("User can't cast vote")
