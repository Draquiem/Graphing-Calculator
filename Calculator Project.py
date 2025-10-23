import math


def add (x,y):
    return x + y
def subtract (x,y):
    return x - y
def multiply (x,y):
    return x * y
def divide (x,y):
    return x / y
def power (x,y):
    return x ** y
def sqrt (x,y):
    return x ** (1 / y)
def factorial(X):
    if x < 0:
        return "Error! Negative Number."
    return.math.factorial(int(X))
def mod(x,y):
    return x % y
def sin(x)
    return math.sin(math.radians(x))
def cos(x)
    return math.cos(math.radians(x))
def tan(x)
    return math.tan(math.radians(x))

print("Select Operation:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Power(x^y)")
print("6.Square Root")
print("7.Factorial")
print("8.Modulus")
print("9.Sine")
print("10.Cosine")
print("11.Tangent")

while true:
    choice = input("Enter your choice (1-11): ")
    if choice in [str(i) for i in range(1, 11)]:
        if choice in ['6','7','9','10','11']
            num = float(input("Enter a number: "))
            if choice == '6':
                print(f"√{num} = {sqrt(num)}")
            elif choice == '7':
                print(f"{int(num)}! = {factorial(num)}")
            elif choice == '9':
                print(f"{int(num)} = {cos(num)}")
            elif choice == '10':
                print(f"{int(num)} = {tan(num)}")
                