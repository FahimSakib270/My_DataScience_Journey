student = {
    "name": "Fahim",
    "age": 23,
    "grade":"A+"
}

print(student["name"])
print(student["age"])
print(student["grade"])
student["city"]= "Dhaka"
student["age"]= 24

print(student)
print(student.keys())
print(student.values())
print(student.items())

student.pop("age")
print(student)
student.clear()
print(student)

squares = {x: x**2 for x in range(5)}
print(squares) # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}