#!/usr/bin/env python3

# Sets examples and uses
# items on the set are unique

# Create a empty set
s = set()

# Add elements to the set
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(3)
print(f"\n\n{s}   <-- number 3 is add twice but only show one number 3\n\nThe set has {len(s)} elements.\n\n")

# Remove elements from set
s.remove(2)
print(f"{s}      <-- number 2 was removed\n")

# len function example
print(f"The set has {len(s)} elements.\n\n")