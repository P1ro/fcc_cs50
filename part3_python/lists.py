#!/usr/bin/env python3


#Using comments now on vid

# List examples and uses

#creating a list with names
names = ["David", "Harry", "Ron", "Hermione", "Ginny"]  

#Print the actual names on console with information
print(f"\n{names} <-- names on a list \nwe will append a new name and and using default sort\n")

#append the name Draco to the list
names.append("Draco")

#Sorting the list alphabetical
names.sort()
print(f"list of names with a new name and sorted alphabetical --> \n{names}\n")
