""" 
Python Data Types: Integers, Floats, Strings
4 of 8 · Escaping Special Characters
"""

""" 
Learn
Sometimes we'll need to create strings containing quotation marks, as in this example: Facebook's old motto was 'move fast and break things'.

In situations like these, we need to alternate double quotation marks (" ") with single quotation marks (' '):

motto = "Facebook's old motto was 'move fast and break things'."
print(motto)

Output
Facebook's old motto was 'move fast and break things'.

Above, we started the string with a double quotation mark. This lets Python know the string ends with the second double quotation mark. As a result, Python considers the single quotation marks in 'move fast and break things' part of the string.

# The string starts with double a quotation mark (")
motto = "Facebook's old motto was 'move fast and break things'."

Copy
However, we may want to surround the motto move fast and break things with double quotation marks: Facebook's old motto was "move fast and break things.". One solution is using single quotation marks to specify the beginning and the ending of the string. However, the single quotation mark in Facebook's will cause Python to think that the string ends there.

# Python won't recognize what comes after 'Facebook'
motto = 'Facebook's old motto was "move fast and break things".'

Copy
Creating the string above will result in a syntax error because Python won't recognize what comes after the string.

motto = 'Facebook's old motto was "move fast and break things".'

Output
SyntaxError: invalid syntax
Fortunately, we can cancel the special function of the second single quotation mark (its special function is to end the string) by typing a backslash character (\) in front of it:

# Notice the backslash character in 'Facebook\'s'
motto = 'Facebook\'s old motto was "move fast and break things".'
print(motto)


Output
Facebook's old motto was "move fast and break things".


The \ character has a special function within a string: it escapes (cancels) the special function of characters. Above, we used \ to escape the second single quotation mark, which had the special function of ending the string.
"""


""" 
Instructions

1. Assign the string Facebook's new motto is "move fast with stable infra." to a variable named motto.
  . Notice there's a . character at the end of Facebook's new motto is "move fast with stable infra." — include the . character in your answer.
  
2. Display the variable motto using print().
"""

motto = 'Facebook\'s new motto is "move fast with stable infra."'

print(motto)