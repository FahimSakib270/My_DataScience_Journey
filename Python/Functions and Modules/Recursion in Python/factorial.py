def factorial(n):
    if n == 1:
     return 1
    return n * factorial(n-1)
print(factorial(5)) 

def fib(n):
   if (n == 0 or n ==1):
      return n
   return fib(n-2)+fib(n-1)
print(fib(6))
