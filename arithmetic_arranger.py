s1 = input("Enter the arithmetic operation you wish to perform (the operator and operands must be seperated by a single space): ")
s2 = input("Enter the arithmetic operation you wish to perform (the operator and operands must be seperated by a single space): ")
s3 = input("Enter the arithmetic operation you wish to perform (the operator and operands must be seperated by a single space): ")
s4 = input("Enter the arithmetic operation you wish to perform (the operator and operands must be seperated by a single space): ")
s5 = input("Enter the arithmetic operation you wish to perform (the operator and operands must be seperated by a single space): ")

s = [s1,s2,s3,s4,s5]
if (len(s) > 5):
    print("Error: Too many problems")
    quit(1)

def arithmetic_arranger(*s, out=True):
    """This function evaluates an arithmetic problem and prints it out in a nice format.
    It takes a list containg only 5 items
    The items in the list must be strings of the problem.
    Example; "3 + 4" can be one of the items in the list.
    This funtion only evaluates addition and subtraction.
    """
    for item in s:
        sl = item.split(" ")

        # Checking the length of the digits 
        if (len(sl[0]) > 4 or len(sl[2]) > 4):
            print("Error! The number of digits cannot be more than 4!")
            quit(1)

        # Making sure the only accpetable operators are + and -
        if ((sl[1] == "+" or sl[1] == "-")):
            pass
        else:
            print("Error! Operator must be + or -.")
            quit(1)

        # Converting the operands to numbers
        al = []
        try:
            al.append(int(sl[0]))
            al.append(int(sl[2]))
        except:
            print("Numbers must contain only digits!")
            quit(1)

        # Checking the operation and evaluating the problem
        if sl[1] == "+":
            ans1 = al[0] + al[1]
        elif sl[1] == "-":
            ans1 = al[0] - al[1]

        # Printing the results
        if out == False:
            pass
        else:
            print(f"{sl[0]  :>8} {'':>4}\n{sl[1] : ^1} {sl[2]  :>6} {'':>4}\n-------- {'':>4}\n{ans1 : >8} {'':>4}\n\n", end="")
            # print(f"{sl[1] : ^1} {sl[2]  :>6} {'':>4}")
            # print(f"-------- {'':>4}")
            # print(f"{ans1 : >8} {'':>4}")

        

arithmetic_arranger(s1,s2,s3,s4,s5)





