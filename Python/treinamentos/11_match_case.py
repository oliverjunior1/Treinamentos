while True:
    choice = int(input("Put a number to see the day and 8 to exit: "))
    match choice:
        case 1:
            print("Sunday")
        case 2:
            print("Monday")
        case 3:
            print("Tuesday")
        case 4:
            print("Wednesday")
        case 5:
            print("Thursday")
        case 6:
            print("Friday")
        case 7:
            print("Saturday")
        case 8:
            break
        case _:
            print("Invalid day, put from 1 to 7: ")

