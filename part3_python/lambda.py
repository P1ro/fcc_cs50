#!/usr/bin/env python3

people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]

#def f(person):
#    return person["name"]

# lambda using inline function 
people.sort(key=lambda person: person["name"])
print(people)