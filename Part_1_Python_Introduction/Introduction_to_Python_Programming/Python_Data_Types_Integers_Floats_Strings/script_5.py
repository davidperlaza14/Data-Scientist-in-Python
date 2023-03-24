""" 
Python Data Types: Integers, Floats, Strings
5 of 8 · String Concatenation

"""

""" 
Learn
When we have two or more distinct strings, it's possible to link them using the + operator:


print('a' + 'b')
print('a' + ' ' + 'b')
print('This' + 'is' + 'a' + 'sentence.')
print('This' + ' ' + 'is' + ' ' + 'a' + ' ' + 'sentence.')

Output
ab
a b
Thisisasentence.
This is a sentence.

We call the process of linking two or more strings together concatenation.

We can also concatenate a string with one or more copies of itself using the * operator followed by a number that specifies how many times to multiply the string:

print('a' * 1)
print('a' * 4)
print('a ' * 5)
print('a' * 0) # No output for this line
print('a' * -1) # No output for this line

Output
a
aaaa
a a a a a

We can't perform arithmetical operations between strings and integers.

print('4' + 1)

Output
TypeError: can only concatenate str (not "int") to str

Likewise, we can't perform arithmetical operations between strings and floats (decimal numbers).

print('4' - 1.0)

Output
TypeError: unsupported operand type(s) for -: 'str' and 'float'

The only exception is when we concatenate a string with copies of itself and use code like 'a' * 2. But that's not an arithmetical operation.
"""

""" 
Instructions

1. Assign the string Facebook's rating is to a variable named facebook.

2. Assign the string 3.5 to a variable named fb_rating_str.

3. Concatenate the strings stored in facebook and fb_rating_str to form the string Facebook's rating is 3.5.

    .Assign the concatenated string to a variable named fb.
    .You'll need to add a space character between Facebook's rating is and 3.5 to avoid ending up with the string Facebook's rating is3.5.
2. Display the fb variable using print().
"""

facebook = "Facebook's rating is"

fb_rating_str = "3.5"

fb = facebook + " " + fb_rating_str

print(fb)