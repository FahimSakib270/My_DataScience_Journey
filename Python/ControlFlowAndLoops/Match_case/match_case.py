a = int(input("please enter a number between 1 and 10 : "))
match a:
    case 1:
        print("the value is 1")
    case 3:
        print("the value is 3")
    case 6: 
        print("the value is 6")
    case _:
        print("value is default")
