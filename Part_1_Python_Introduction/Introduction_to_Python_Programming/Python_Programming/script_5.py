""" 
Python Programming
6 of 8 · Code Comments
"""

""" 
Learn
The computer executes code from the first line downward and ignores blank lines. Let's display some information about Fruit Ninja Classic to demonstrate this:

print(1.99)
print(698516)
print(4.5)

Output
1.99
698516
4.5


Besides blank lines, the computer also ignores any sequence of characters that comes to the right of the # symbol. In the example below, we use # before print(1.99), and we see the output of print(1.99) no longer displays — this is because print(1.99) isn't executed when # precedes it.

#print(1.99)
print(698516)
print(4.5)

Output
698516
4.5

The sequence of characters that follows the # symbol is a code comment. We can use code comments to add information about our code:

print(1.99) # App cost for Fruit Ninja Classic
print(698516) # Rating count
print(4.5) # Average user rating


Output
1.99
698516
4.5

Another way we can use code comments is adding a general description at the beginning of our program.

# Fruit Ninja Classic app cost, rating count, and user rating
print(1.99)
print(698516)
print(4.5)

Output
1.99
698516
4.5

Now let's practice using code comments.


"""

""" 
Instructions
In the code editor on the right, we've provided these four lines of code:

"""

# Minecraft: Pocket Edition cost, rating count, and user rating
print(6.99)
print(522012) 
print(4.5)

""" 
1. Uncomment the three lines of code that specify print() by removing the # symbols, and then click the Submit Answer button.

  . Do not uncomment the first line of code, which includes the general description.
  
  
Note that if we do not specify a code comment (#) before (to the left of) the general description, the code will result in a syntax error.
"""