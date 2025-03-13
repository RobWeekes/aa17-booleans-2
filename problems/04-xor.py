# Create a function that returns the `xor` result of two values.

# Are the results a bit confusing when integer values are passed in? You can
# learn more about Python's bitwise operators in the python wiki.
# https://wiki.python.org/moin/BitwiseOperators

# Write your function here.

# this works w booleans but not integers
# def xor(val1, val2):
#   if val1 is True and val2 is False:
#     return True
#   elif val1 is False and val2 is True:
#     return True
#   else:
#     return False

# using python's built-in XOR operator ^
def xor(val1, val2):
  return val1^val2

print(xor(False, False))   #>  False
print(xor(True, False))   #>  True
print(xor(False, True))   #>  True
print(xor(True, True)) #>  False
print('bitwise operators:')
print(xor(5, 3))  #> 6
print(xor(8, 4))  #> 12
print(xor(2, 2))  #> 0
print(xor(1, 2))  #> 3
print(xor(4, 4))  #> 0

# Print binary representations
print(bin(5))  # Output: 0b101
print(bin(3))  # Output: 0b11

# Print 8-bit binary representation
print(format(5, '08b'))  # Output: 00000101
print(format(3, '08b'))  # Output: 00000011

# The '08b' format specifier means:
# b: binary format
# 0: pad with zeros
# 8: use 8 digits
# This makes it easier to visualize the bitwise operations we're performing in the XOR examples.
