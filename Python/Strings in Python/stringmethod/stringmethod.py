name = "fahim"
print(len(name))
print(name.upper())
print(name.lower())
print(name.strip())
print(name.replace("fahim","sakib"))
print(name.split())
print(name.capitalize())


# text = "  hello world  "
# print(text.strip()) # Output: "hello world"
# print(text.lstrip()) # Output: "hello world  "
# print(text.rstrip()) # Output: "  hello world


# text = "Python is fun"
# print(text.find("is"))
# print(text.replace("Python","java"))


# text = "apple,banana,orange"

# print(text.split())
# print("".join(text))

text = "Python123"
print(text.isalpha()) # Output: False
print(text.isdigit()) # Output: False
print(text.isalnum()) # Output: True
print(text.isspace()) # Output: False