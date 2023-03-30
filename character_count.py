# Count the number of times each character appears in a string

def char_count(string):
    mydict = {}
    for i in string:
        if i in mydict:
            mydict[i] += 1
        else:
            mydict[i] = 1

    return mydict

if __name__ == "__main__":
    strn = "Thecleverprogrammer"
    new = char_count(strn)
    print(new)