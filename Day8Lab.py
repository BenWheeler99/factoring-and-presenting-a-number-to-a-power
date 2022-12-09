# Program to use functions
#
# Written by Ben Wheeler
# Culver-Stockton College    12/9/2022

# Function to compute x to the k power
def power(x,k):
    n = 1
    base = x
    while n != k:
        n = n + 1
        x = x * base
    return x
# Function to compute the factorial of an integer  
def factorial(num):
    if num < 0:
         print('Number must be >= 0')
         return 0
    else:
           fac = 1
           while num >= 1:
                fac = fac * num
                num = num - 1
    return fac
# Main program
x = float(input("Enter x value "))
k = int(input("To what power? "))
n = int(input("Enter n value "))
facto = factorial(n)
exp = power(x,k)
result = round(100*(facto/exp))/100
print(str(facto) + " is the factorial")
print(str(exp) + " is the exponential value")
print(str(result) + " is the result")
