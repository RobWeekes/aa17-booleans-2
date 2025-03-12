# Write a function using the `not` and `or` operator that returns the Boolean
# result of the `not` and `or` operator being applied to the function's
# arguments.

# Write your function here.

# don't forget the result changes if 'not' applies to both args in (parenthesis), or just the first argument with no ( )

# def not_or(arg1, arg2):
#   return not (arg1 or arg2)

# False
# False
# False
# True

def not_or(arg1, arg2):
  return not arg1 or arg2

print(not_or(True, False))    #> False
print(not_or(True, True))     #> True
print(not_or(False, True))    #> True
print(not_or(False, False))   #> True
