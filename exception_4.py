class InvalidValue(Exception):
    pass
try :
    username = str(input("Enter username"))
    # arr = []
    # for i in range(3):
    password = str(input("Enter Password"))
        # arr.append(password)
    pass1 = str(input("Enter the password Again"))
    if len(username)<6 or pass1 not in password:
        raise InvalidValue
    else :
        print(username)
        print(password)
except InvalidValue:
    print("Invalid Password and Username")
except ValueError:
    print("Enter correct values")
