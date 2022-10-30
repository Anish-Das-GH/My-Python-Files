class Polygon:

    def __init__(self, n):
        self.number_of_sides = n

class rectangle(Polygon):
    def __init__(self,breadth,length):
        Polygon.__init__(self, 4)
        print("No of sides in rectangle is :",self.number_of_sides)
        self.breadth=breadth
        self.length=length
    def area(self):
        return self.breadth*self.length

class triangle(Polygon):
    def __init__(self,a,b,c):
        Polygon.__init__(self, 3)
        print("No of sides in rectangle is :", self.number_of_sides)
        self.a = a
        self.b = b
        self.c = c
    def area(self):
        s =  (self.a+self.b+self.c) / 2
        return ((s*(s-self.a)*(s-self.b)*(s-self.c)) ** 0.5)


Breadth=int(input("Enter length of rectangle: "))
Length=int(input("Enter breadth of rectangle: "))
rec=rectangle(Breadth,Length)
print("Area of rectangle: ",rec.area())

a = float(input('Enter first side of Triangle: '))
b = float(input('Enter second side of Triangle: '))
c = float(input('Enter third side of Triangle: '))
tri = triangle(a,b,c)
print("Area of Triangle : ",tri.area())
