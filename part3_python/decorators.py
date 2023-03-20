#!/usr/bin/env python3

# Decorator example, use a function to check and run another function
def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done with the function.")
    return wrapper

@announce
def hello():
    print("Hellow, world!")

hello()