def func(x):
    f = ((x*x*x)+2*x*x+x-1)
    return f

def deriv(x):
    f = ((3*x*x)+4*x+1)
    return f


def bisection():
    a = 0 
    b = 2
    k = 1
    while True:
        x = (a+b)/2
        if(abs(func(a))<0.000001):
            # print("The root = ",a)
            break
        elif(abs(func(b))<0.000001):
            # print("The root = ",b)
            break
        if(abs(func(x))<0.00001):
            # print("The root = ",x)
            break
        elif(func(a)*func(x)<0):
            b = x
        else:
            a = x
    return x

def newton():
    a = 1
    while True:
        x = a - func(a)/deriv(a)
        if(abs(func(a))<0.00001):
            # print("The root = ",a)
            break
        elif(abs(func(x))<0.00001):
             # print("The root = ", x)
            break
        else:
            a = x
    return x
    
def secant():
    a = 1
    b = 2
    while True:
        x = (a*func(b)-b*func(a))/(func(b)-func(a))
        if(abs(func(a))<0.00001):
            # print("The root = ",a)
            break
        elif(abs(func(b))<0.00001):
            # print("The root = ",b)
            break
        elif(abs(func(x))<0.00001):
            # print("The root = ",x)
            break
        else:
            a = b
            b = x
    return x

print("1. Use bisection method")
print("2. Use Newton Raphson's method")
print("3. Use Secant method")
x = input("Choose from the options above, the method you want to use: ")
try:
    y = int(x)
except:
    print("Enter a numeric value that corresponds to one of the options given")
    quit()
if(y == 1):
    ans = bisection()
    print("The root = ",ans)
elif(y == 2):
    ans = newton()
    print("The root = ", ans)
elif(y == 3):
    ans = secant()
    print("The root = ", ans)
elif(y == 4):
    quit()
else:
    print("Enter a number that corresponds to one of the options given")