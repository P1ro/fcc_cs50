#!/usr/bin/env python3

#Sequences and selecting especific items

#Select item on a string
name = "David"      #This variable is a string
print(f"Select letters of {name} wich is a str")
#python start couunting from 0
print(name[0])  #choose fist letter     "D"
print(name[1])  #choose second letter   "a"
print(name[2])  #choose Thrird          "v"
print(name[3])  #choose fourth          "i"
print(name[4])  #choose five            "d"
#This might give you the idea of how this work, theres more 
#when selecting can be using a identifier and move back or front
print("") #using this print instead of \n just to keep it clean

#Select item on a list pretty much the same
names = ["David", "Harry", "Ron", "Hermione"]
print(f"Select Each name from {names} wich is a list")
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print("") #using this print instead of \n just to keep it clean

#Select from a tuple
coordinate = (10.0, 20.0) #tuple
print(f"select item from the tuple coordinate {coordinate} wich is a tuple")
print(f"coordinateX = {coordinate[0]}")
print(f"coordinateY = {coordinate[1]}")
print("")

#Data Structures 
print("Data Structures")
print("List = sequence of muteable values")
print("tuple = sequence of immutable values")
print("set = collection of unique values")
print("dict = collection of key-value paris")
