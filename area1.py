height = 0.0
width = 0.0
length = 0.0
base = 0.0
radius = 0.0
n = 1


def triangle(height,base) :
    try:
        h = input("Enter the value of the height: ")
        b = input("Enter the value of the base: ")
        height = float(h)
        base = float(b)
    except:
        print("Please enter numeric values!")
        quit()
    area = (height*base)/2
    return area
    

def rect(length,width) :
    try:
        l = input("Enter the value of the length: ")
        w = input("Enter the value of the width: ")
        length = float(l)
        width = float(w)
    except:
        print("Please enter numeric values!")
        quit()
    area =length*width
    return area


def circ(radius):
    try:
        r = input("Enter the value of the radius: ")
        radius = float(r)
    except:
        print("Please enter a numeric value!")
        quit()
    PI = 3.14
    area = PI*(radius*radius)
    # print("The area of the Circle = ", area)
    return area


while n != 4:
    print("""Choose the option you want
1. Area of a Triangle
2. Area of a Rectangle
3. Area of a circle
4. Exit""")
    print()

    try:
        n = input("Enter the number that corresponds to the choice you want: ")
        nn = int(n)
    except:
        print("""ERROR!!!
Enter a numeric value that corresponds to the choice you want""")
        quit()


    if nn == 1:
        ans = triangle(height,base)
        print("The area of the Triangle = ", ans)
    elif nn == 2:
        ans = rect(length,width)
        print("The area of the triangle = ", ans)
    elif nn == 3:
        ans = circ(radius)
        print("The area of the circle = ", ans)
    elif nn == 4:
        break
