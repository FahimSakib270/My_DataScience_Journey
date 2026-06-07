# fname = "Fahim"
# lname = "sakib"

# fullname = fname +" "+ lname
# print(fullname)


# """Given text = "Python Programming", do the following:
# Print the first 6 characters
# Print the last 6 characters
# Print every second character from the string
# Reverse the string text using slicing."""

# text = "Python Programming"
# print(text[:6])
# print(text[-6:])
# print(text[::2])
# print(text[::-1])

"""3. String Methods and Functions
Take the string "  i love python programming  " and:

Remove extra spaces from both ends
Convert it to title case
Count how many times "o" appears
Check if the string "123abc" is alphanumeric."""

text = "  i love python programming  "

print(text.strip())

print(text.title())

total = 0
for i in text:
    if i == "o":
        total=total+1

print(total)

print(text.count("o"))
print("123abc".isalnum())