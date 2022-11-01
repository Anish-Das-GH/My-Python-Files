class circle:

    PI = 3.14

    def __init__(self,radius):
        self.radius = radius

    def Circumference(self):
        return (2*self.PI*self.radius)
    def Area(self):
        return (self.PI*self.radius*self.radius)

r = float(input("Enter Radius"))
c1 = circle(r)

print(c1.Area())
print(c1.Circumference())