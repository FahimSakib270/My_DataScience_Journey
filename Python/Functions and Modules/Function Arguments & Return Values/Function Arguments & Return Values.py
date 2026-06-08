def add (a,b):
    total = a+b
    return total

o1 = add(2,3)
print(o1)

def add2 (a,b,plus = 0):
    total = a+b+plus
    return total

o1 = add(2,3)
o2 = add2(2,3,4)
print(o1)
print(o2)


def profile(name,age):
    greet = f"my name is {name}. I am {age}"
    return greet

profile1 = profile(age=23, name="Fahim")
print(profile1)

square = lambda x:x*x
print(square(4))

sumlamda = lambda x,y:x+y
print(sumlamda(2,3))