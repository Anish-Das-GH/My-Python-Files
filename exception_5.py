class Booknotfound(Exception):
    pass
try:
    n = int(input("Enter no of books"))
    arr = []
    for i in range(n):
        book = str(input("Enter name of books"))
        arr.append(book)
    search=str(input("Enter book name u wanna search"))
    if search in arr:
        print("Book Found")
    else :
        raise Booknotfound
except Booknotfound:
    print("Book not Found")
except ValueError:
    print("ENter correct book name")