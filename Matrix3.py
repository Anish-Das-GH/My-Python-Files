Student_dt = [ [72, 85, 87, 90, 69], [80, 87, 65, 89, 85], [96, 91, 70, 78, 97], [90, 93, 91, 90, 94], [57, 89, 82, 69, 60] ]

for x in Student_dt:  # outer loop
    for i in x:  # inner loop
        print(i, end = " ") # print the elements
    print()