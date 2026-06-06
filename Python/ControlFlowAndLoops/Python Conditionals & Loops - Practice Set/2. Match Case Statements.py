# # # Ask the user to enter a day number (1–7) and print the corresponding day of the week using match case.

# # dayName = int(input("enter day number "))

# # match dayName:
# #     case 1:
# #         print("saturday")
# #     case 2:
# #         print("sun")
# #     case 3:
# #         print("mon")
# #     case 4:
# #         print("tues")
# #     case 5:
# #         print("wed")
# #     case 6:
# #         print("thus")
# #     case 7:
# #         print("friday")
# #     case _:
# #         print("error input")


# # Write a program using match case that simulates a simple calculator.

# # Ask the user for two numbers and an operation (+, -, *, /).
# # Perform the operation using match case.

# num1 = float(input("Enter 1st number "))
# num2 = float(input("Enter 2nd number "))

# operation = input("Enter an operation (+,-,*,/) ")

# match operation:
#     case "+":
#         print(num1+num2)
#     case "-":
#         print(num1-num2)
#     case "*":
#         print(num1*num2)
#     case "/":
#         print(num1/num2)
#     case _:
#         print("enter a right operation")
