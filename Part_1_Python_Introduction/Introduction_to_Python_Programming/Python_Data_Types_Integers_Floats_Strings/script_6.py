""" 
Python Data Types: Integers, Floats, Strings
6 of 8 · String Conversion
"""

""" 
Learn
If the strings contain characters that form a valid number (like '4', '3.3', '12', etc.), it's possible to convert them to integers or floats first, and then do the arithmetical operations. We can use the int() or float() function to convert a string of type str to a number of type int or float.

print(int('4') + 1)
print(float('3.3') + 1)

Output
5
4.3

But attempting to convert a str to an int won't work:

Output
ValueError: invalid literal for int() with base 10: 'wrong format'

Note that we can also convert an int or a float to a str using the str() function. In doing so, it will now have properties of a string as demonstrated below.

a = 2
b = 5

print(a+b)
print(str(a)+str(b))

Output
7
25

Notice that while the addition of the integers printed the sum of a and b, when converted into a string by the str() function it printed the concatenation of the strings instead.
"""

""" 
Instructions

1. Assign the string Facebook's rating is to a variable named facebook.

2. Assign the float 3.5 to a variable named fb_rating.

3. Convert fb_rating from a float to a string using the str() function, and assign the converted value to a new variable named fb_rating_str.
4. Concatenate the strings stored in facebook and fb_rating_str to form the string Facebook's rating is 3.5.
    . Assign the concatenated string to a variable named fb.
    . You'll need to add a space character between Facebook's rating is and 3.5 to avoid ending up with the string Facebook's rating is3.5.
5. Display the fb variable using print().

"""

facebook = "Facebook's rating is"

fb_rating = 3.5

fb_rating_str = str(fb_rating)

fb = facebook + " " + fb_rating_str

print(fb)
