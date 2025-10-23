import math

def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b
def power(a, b): return a ** b
def root(a, n=2):
    if a < 0 and n % 2 == 0:
        raise ValueError("Even root of a negative number is not real.")
    return a ** (1.0 / n)
def factorial(n):
    if n < 0 or int(n) != n:
        raise ValueError("Factorial needs a non-negative integer.")
    return math.factorial(int(n))
def mod(a, b): return a % b
def sin_deg(x): return math.sin(math.radians(x))
def cos_deg(x): return math.cos(math.radians(x))
def tan_deg(x): return math.tan(math.radians(x))

# --- Menu ---
print("Select Operation:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Power(a^b)")
print("6.Square Root")
print("7.Factorial")
print("8.Modulus")
print("9.Sine (degrees)")
print("10.Cosine (degrees)")
print("11.Tangent (degrees)")
print("0.Exit")

valid = {str(i) for i in range(1, 12)}     
single_input = {'6', '7', '9', '10', '11'}

while True:
    choice = input("Select your operation :3 | hit 0 to close (0–11): ").strip()

    if choice == '0':
        print("Hasta la pasta m8!")
        break

    if choice not in valid:
        print("This input is invalid man... Try again.")
        continue

    try:
        if choice in single_input:
            x = float(input("Enter a number: "))
            if choice == '6':
                result = root(x, 2)                 
                print(f"√{x} = {result}")
            elif choice == '7':
                result = factorial(x)
                print(f"({int(x)}!) = {result}")
            elif choice == '9':
                result = sin_deg(x)
                print(f"sin({x}°) = {result}")
            elif choice == '10':
                result =cos_deg(x)
                print(f"cos({x}°) = {result}")
            elif choice == '11':
                result =tan_deg(x)
                print(f"tan({x}°) = {result}")
        else:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            if choice == '1':
                result = add(a, b)
                if result == int(69):
                    print("Nice.") ## Hehe.
                print(f"({a} + {b}) = {result}")
            elif choice == '2':
                result =subtract(a, b)
                print(f"({a} - {b}) = {result}")
            elif choice == '3':
                result =multiply(a, b)
                print(f"({a} * {b}) = {result}")
            elif choice == '4':
                result =divide(a, b)
                print(f"({a} / {b}) = {result}")
            elif choice == '5':
                result =power(a, b)
                print(f"({a}^{b}) = {result}")
            elif choice == '8':
                result =mod(a, b)
                print(f"({a} % {b}) = {result}")
    except Exception as e:
        print(f"Error: {e}")
