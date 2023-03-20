#!/usr/bin/env python3
# 
from functions import square
# import functions  #import all functions module and call the funtion with a dot "."
print(f"\n # Calling the square function from functions.py using range(10)\n")
for i in range(10):
    print(f"The square of {i} is {square(i)}")