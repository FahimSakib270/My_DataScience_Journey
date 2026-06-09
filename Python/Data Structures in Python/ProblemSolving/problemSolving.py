# """Create a list fruits = ["apple", "banana", "cherry"].
# Print the first fruit.
# Replace "banana" with "orange".
# Print the length of the list."""

# fruits = ["apple","banana","cherry"]
# print(fruits[0])
# fruits[1]= "orange"
# print(fruits)
# print(len(fruits))

# """Create a list of numbers from 1 to 10.

# Print the first three numbers using slicing.
# Print the last three numbers using slicing."""

# numbers = [1,2,3,4,5,6,7,8,9,10]
# print(numbers[0:3])
# print(numbers[len(numbers)-3:])

"""List Methods
Start with numbers = [5, 2, 9, 1, 7] and do the following:

Sort the list in ascending order.
Append the number 10 to the list.
Remove the number 2 from the list.
Create a list names = ["Alice", "Bob", "Charlie"] and use the insert() method to add "David" at index 1.

"""
# numbers = [5, 2, 9, 1, 7]
# numbers.sort()
# print(numbers)
# numbers.append(10)
# print(numbers)
# numbers.remove(2)
# print(numbers)
# names = ["Alice", "Bob", "Charlie"]
# names.insert(1,"david")

"""Create a dictionary student = {"name": "John", "age": 20, "grade": "A"} and:

Print the value of "name".
Change "grade" to "A+".
Add a new key "city" with value "Delhi".
Create a dictionary of three friends and their phone numbers. Use:

keys() to get all names
values() to get all numbers
items() to loop over key-value pairs and print them
"""
student = {"name": "John", "age": 20, "grade": "A"}

print(student["name"])
student["grade"]= "A+"
student["City"] = "delhi"
