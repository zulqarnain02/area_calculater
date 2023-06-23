def calculate_area():
    i="YES"
    while i=="YES":
        print("Select a number of a perticular shape: ") 
 
        print("1.Circle")
        print("2.Triangle")
        print("3.Square")
        print("4.Rectangle")
        print("5.Parallelogram")
        print("6.Trapezium")
        print("7.Ellipse")
        print("8.Cube")
        print("9.Rectangular prism")
        print("10.Cylinder")
        print("11.Cone")
        print("12.Sphere")
        print("13.Hemisphere")
        pi=22/7
        n=int(input())
        if n==1:
            i=int(input("Enter value of radius:"))
            q=pi*i*i
            print("Area of circle is:",q)
        elif n==2:
            i=int(input("Enter the value of base: "))
            j=int(input("Enter the value of height: "))
            a=0.5*i*j
            print("Area of triangle is:",a)
        elif n==3:
            i=int(input("Enter value of side:"))
            q=i*i
            print("Area of square is:",q)
        elif n==4:
            i=int(input("Enter value of length:"))
            j=int(input("Enter value of width:"))
            q=i*j
            print("Area of rectangle is:",q)
        elif n==5:
            i=int(input("Enter value of base:"))
            j=int(input("Enter value of vertical height"))
            q=i*j
            print("Area of parallelogram is:",q)
        elif n==6:
            i=int(input("Enter value of length of one parallel side:"))
            j=int(input("Enter value of length of other parallel side:"))
            h=int(input("Enter value of perpendicular height:"))
            q=(0.5*(i+j))*h
            print("Area of trapezium is:",q)
        elif n==7:
            i=int(input("Enter value of 1/2 of minor axis:"))
            j=int(input("Enter value of 1/2 of major axis:"))
            q=pi*i*j
            print("Area of ellipse is:",q)
        elif n==8:
            i=int(input("Enter value of length of edge:"))
            q=6*i*i
            print("Area of cube is:",q)
        elif n==9:
            i=int(input("Enter value of length:"))
            w=int(input("Enter value of width:"))
            h=int(input("Enter valie of height:"))
            q=2*(i*w+i*h+w*h)
            print("Area of rectangular prism is:",q)
        elif n==10:
            i=int(input("Enter value of radius of circular base: "))
            j=int(input("Enter valie of height of cylinder: "))
            q=2*pi*(i+j)
            print("Area of cylinder is:",q)
        elif n==11:
            i=int(input("Enter value of radius of circular base:"))
            j=int(input("Enter value of slant height:"))
            q=pi*i*(i+j)
            print("Area of cone is:",q)
        elif n==12:
            i=int(input("Enter value of radius:"))
            q=4*pi*i*i
            print("Area of sphere is:",q)
        elif n==13:
            i=int(input("Enter value of radius of hemisphere:"))
            q=3*pi*i*i
            print("Area of hemisphere is:",q)
        else:
            print("Sorry you have selected option which is not in above list.")
            print()
            print("Retry")
            print()
            calculate_area()
 
            print()
            print("Do you want to find areas of different shapes")
            print("Enter")
            i=input("YES to continue and NO to exit the area calculator: ")
            i=i.upper()
            print()
            if i=="NO":
                print("Thank you for using AREA CALCULATOR")
            else:
                print("Invalid input")
                print("Enter YES to continue and NO to exit")
                i=input()
                i=i.upper()
                while i!="YES":
                    print("Invalid input ")
                    print("Try again ")
                    i=input("YES to continue and NO to exit the area calculator: ")
                    i=i.upper()
                    if i=="YES":
                        calculate_area()
                    elif i=="NO":
                        print("Thank you for using AREA CALCULATOR")
 
                        print("                 Area Calculator                  :")
                        print()
                        calculate_area()
