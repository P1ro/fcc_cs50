#!/usr/bin/env python3
import sys


# Error handle examples
    
# invalid input expect a number
try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Error: Invalid input.")
    sys.exit(1)

# Invalid division by 0 
try:
    result = x / y
except ZeroDivisionError:
    print("Error: Cannot divide by 0.")
    sys.exit(1)
print(f"{x} / {y} = {result}")