def add_time(start, duration, day = None):
    """
    This function takes the start time, the duration and an optional day argument and calcutes the \
    time after the given duration using the 12-hour time format.
    The inputs are strings
    """
    # Converting the hour and minute components of the start time to integers
    s1 = start.split(":")
    s2 = s1[1].split(" ")
    s1[0] = int(s1[0])
    s2[0] = int(s2[0])

    # Converting the hour and minute components of the duration to integers
    t1 = duration.split(":")
    t1[0] = int(t1[0])
    t1[1] = int(t1[1])
    if t1[1] > 60:
        print("The minutes cannot be more than 60!")
        quit(1)

    # Calculating the total hours
    hours = s1[0] + t1[0]

    # Calculating the hours using the 12-hour format
    rem = hours % 12   
    days = hours // 24
  
    # Calculating the minutes. If the minutes exceed the maximum (60), it is added to the hours
    minutes = s2[0] + t1[1]
    if minutes > 60:
        minutes = minutes % 60
        rem += 1

    # Calculating the number of hours left after taking the days out
    rem_2 = t1[0] % 24

    # Conditions to print the result in the desired format
    if day == None:
        if (hours < 12 and s2[1] == "PM"):
            print(f"{rem:02d}:{minutes:02d} PM")
        elif (hours < 12 and s2[1] == "AM"):
            print(f"{rem:02d}:{minutes:02d} AM")
        elif (hours >= 12 and hours < 24 and s2[1] == "PM"):
            print(f"{rem:02d}:{minutes:02d} AM (next day)")
        elif (hours >= 24 and rem_2 == 0 and s2[1] == "PM"):
            print(f"{rem:02d}:{minutes:02d} PM ({days} days later)")
        elif (hours >= 24 and rem_2 == 0 and s2[1] == "AM"):
            print(f"{rem:02d}:{minutes:02d} AM ({days} days later)")
        elif (hours >= 24 and rem_2 != 0 and rem_2 >= 12 and (s1[0] + rem_2 >= 12) and s2[1] == "PM"):
            print(f"{rem:02d}:{minutes:02d} AM ({days} days later)")
        elif (hours >= 24 and rem_2 != 0 and rem_2 >= 12 and (s1[0] + rem_2 >= 12) and s2[1] == "AM"):
            print(f"{rem:02d}:{minutes:02d} PM ({days} days later)")
        elif (hours >= 24 and rem_2 != 0 and rem_2 >= 12 and s2[1] == "PM"):
            print(f"{rem:02d}:{minutes:02d} PM ({days} days later)")
        elif (hours >= 24 and rem_2 != 0 and rem_2 >= 12 and s2[1] == "AM"):
            print(f"{rem:02d}:{minutes:02d} AM ({days} days later)")
        elif (hours >= 24 and rem_2 != 0 and rem_2 < 12 and (s1[0] + rem_2 >= 12) and s2[1] == "PM"):
            print(f"{rem:02d}:{minutes:02d} AM ({days} days later)")
        elif (hours >= 24 and rem_2 != 0 and rem_2 < 12 and (s1[0] + rem_2 >= 12) and s2[1] == "AM"):
            print(f"{rem:02d}:{minutes:02d} PM ({days} days later)")
        elif (hours >= 24 and rem_2 != 0 and rem_2 < 12 and s2[1] == "PM"):
            print(f"{rem:02d}:{minutes:02d} PM ({days} days later)")
        elif (hours >= 24 and rem_2 != 0 and rem_2 < 12  and s2[1] == "AM"):
            print(f"{rem:02d}:{minutes:02d} AM ({days} days later)")
    elif day != None:
        if (hours < 12 and s2[1] == "PM"):
            print(f"{rem:02d}:{minutes:02d} PM {day.capitalize()}")
        elif (hours < 12 and s2[1] == "AM"):
                print(f"{rem:02d}:{minutes:02d} AM {day.capitalize()}")
        elif (hours >= 12 and hours < 24 and s2[1] == "PM"):
                print(f"{rem:02d}:{minutes:02d} AM (next day)")
        elif (hours >= 24 and rem_2 == 0 and s2[1] == "PM"):
            print(f"{rem:02d}:{minutes:02d} PM {day.capitalize()} ({days} days later)")
        elif (hours >= 24 and rem_2 == 0 and s2[1] == "AM"):
            print(f"{rem:02d}:{minutes:02d} AM {day.capitalize()} ({days} days later)")
        elif (hours >= 24 and rem_2 != 0 and rem_2 >= 12 and (s1[0] + rem_2 >= 12) and s2[1] == "PM"):
            print(f"{rem:02d}:{minutes:02d} AM {day.capitalize()} ({days} days later)")
        elif (hours >= 24 and rem_2 != 0 and rem_2 >= 12 and (s1[0] + rem_2 >= 12) and s2[1] == "AM"):
            print(f"{rem:02d}:{minutes:02d} PM {day.capitalize()} ({days} days later)")
        elif (hours >= 24 and rem_2 != 0 and rem_2 >= 12 and s2[1] == "PM"):
            print(f"{rem:02d}:{minutes:02d} PM {day.capitalize()} ({days} days later)")
        elif (hours >= 24 and rem_2 != 0 and rem_2 >= 12 and s2[1] == "AM"):
            print(f"{rem:02d}:{minutes:02d} AM {day.capitalize()} ({days} days later)")
        elif (hours >= 24 and rem_2 != 0 and rem_2 < 12 and (s1[0] + rem_2 >= 12) and s2[1] == "PM"):
            print(f"{rem:02d}:{minutes:02d} AM {day.capitalize()} ({days} days later)")
        elif (hours >= 24 and rem_2 != 0 and rem_2 < 12 and (s1[0] + rem_2 >= 12) and s2[1] == "AM"):
            print(f"{rem:02d}:{minutes:02d} PM {day.capitalize()} ({days} days later)")
        elif (hours >= 24 and rem_2 != 0 and rem_2 < 12 and s2[1] == "PM"):
            print(f"{rem:02d}:{minutes:02d} PM {day.capitalize()} ({days} days later)")
        elif (hours >= 24 and rem_2 != 0 and rem_2 < 12  and s2[1] == "AM"):
            print(f"{rem:02d}:{minutes:02d} AM {day.capitalize()} ({days} days later)")





# Taking inputs from the user
s1 = input("Enter the start time: ")
t1 = input("Enter the duration: ")
check = input("Press y to enter the day of the week and n to ignore: ")
if (check == "y" or check == "Y"):
    day = input("Enter the day of the week: ")
elif (check == "n" or check == "N"):
    day = None


add_time(s1,t1,day=day)










