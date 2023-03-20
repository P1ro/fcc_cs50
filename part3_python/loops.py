#!/usr/bin/env python3

# Comments only prints on terminal information
# to avoid code duplication
# and can be read on the code.

print("\n # Basic loop of a list example.")
for i in [0, 1, 2, 3, 4, 5]:
    print(i)

print("\n # Loop a variable containing a list.")
numberlist = [0, 1, 2, 3, 4, 5]
for x in numberlist:
    print(x)

print("\n # Loop using a range function.")
for y in range(6):
    print(y)

print("\n # loop over list of names." )
names = ["David", "Harry", "Ron", "Hermione", "Ginny"]
for name in names:
    print(name)

print("\n # loop over character on a string.")
name = "David"
for character in name:
    print(character)