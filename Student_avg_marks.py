class Student :
    def getstudentdetails(self):
        self.roll = input("Enter The Roll no of the student ")
        self.name = input("What's the name of the student ? ")
        self.phy = int(input("Enter the marks of Physics "))
        self.chem = int(input("Enter the marks of Chemistry "))
        self.math = int(input("Enter the marks of Math "))

    def Printresults(self):
        self.average = int((self.phy+self.chem+self.math)/3)
        print("Name : ",self.name)
        print("Average Marks : ",self.average)
# Student1
S1=Student()
S1.getstudentdetails()


S1.Printresults()

# Student 2
S2=Student()
S2.getstudentdetails()


S2.Printresults()

# Student 3

S3=Student()
S3.getstudentdetails()


S3.Printresults()


# Student 4

S4=Student()
S4.getstudentdetails()


S4.Printresults()

