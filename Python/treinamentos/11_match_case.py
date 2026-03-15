while True:
    day = int(input("Put the number to 1 to 7 to see the day, and 8 to exit: "))
    match day:
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
            print("Wrong number, put 1 to 8 to obtain a result!")
