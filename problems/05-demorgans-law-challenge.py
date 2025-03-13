# Create a function that uses DeMorgan's Law to get the expected `True`/`False`
# statement.

# Write your function here.

def de_morgans_law(val1,val2):
  return not val1 or not val2

print(de_morgans_law(True, True)) # False
print(de_morgans_law(True, False)) # True
print(de_morgans_law(False, False)) # True
print(de_morgans_law("", [])) # True
print(de_morgans_law(2, 2)) # False
print(de_morgans_law(2, 0)) # True


# DeMorgan's Law is a logical principle that states:

# NOT (A AND B) equals (NOT A) OR (NOT B)
# NOT (A OR B) equals (NOT A) AND (NOT B)

# The test cases show how it works with different types:

# Boolean values (True/False)
# Empty sequences ("", [])
# Numbers (2, 0)
# In Python:

# Empty sequences, 0, None, and False are "falsy"
# Non-empty sequences, non-zero numbers, and True are "truthy"
# That's why de_morgans_law("", []) returns True - both inputs are empty sequences which are falsy, so their negation with not becomes True.
