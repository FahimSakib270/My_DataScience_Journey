"""1.Write a function greet() that prints "Hello, Python Learner!" when called.
Write a function square(num) that returns the square of a given number. Test it with different numbers."""

def greet():
    print("Hello python learner!")

greet()

def square(num):
    return num*num

print(square(8))

"""2. Function Arguments & Return Values
Write a function full_name(first, last) that takes first name and last name as parameters and returns a single string in the format "First Last".

Write a function calculate_area(length, width=10) that returns the area of a rectangle. Test it by calling the function with:

Both length and width
Only length (use default width)"""

def fullName (fname,lname):
    return f"{fname} {lname}"

print(fullName("Fahim","Sakib"))

def area(l,w=10):
    return l*w

print(area(4))


"""3. Lambda Functions
Write a lambda function that adds two numbers and test it.
Create a list [1, 2, 3, 4, 5] and use map() with a lambda function to get their squares."""

add = lambda x,y:x+y
print(add(3,4))

# Create the list
numbers = [1, 2, 3, 4, 5]

# Use map() with a lambda function to get squares
squares = list(map(lambda x: x ** 2, numbers))

# Display the result
print(squares)  


"""4. Recursion in Python
Write a recursive function factorial(n) that returns the factorial of a number.
Write a recursive function sum_of_digits(n) that returns the sum of all digits of a given number."""

def factorial(n):

    # Base case: factorial of 0 or 1 is 1
    if n <= 1:
        return 1
    # Recursive case: n * factorial of (n-1)
    else:
        return n * factorial(n - 1)

print(f"factorial(5) = {factorial(5)}")    
print(f"factorial(0) = {factorial(0)}")

def sum_of_digits(n):
    
    # Take absolute value to handle negative numbers
    n = abs(n)
    
    # Base case: if number is single digit, return the number itself
    if n < 10:
        return n
    else:
        return (n % 10) + sum_of_digits(n // 10)

# Test the sum_of_digits function
print(f"sum_of_digits(12345) = {sum_of_digits(12345)}")    
