class Circle:
    PI = 3.14

    def __init__(self,radius):
        self.radius = radius

    def Area(self):
        return (Circle.PI * self.radius * self.radius)

    def Circumference(self):
        return (2 * Circle.PI * self.radius)

r = int(input("Enter the radius of circle "))
c1 = Circle(r)
print ("The area of C1 circle is: ", c1.Area())
print ("Circumference of C1 Circle is: ", c1.Circumference())
print("")
