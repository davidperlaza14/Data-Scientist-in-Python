""" Programming Python Variables
3 of 6 · Variable Names"""

""" 
Learn

On the previous screen, we learned that we can choose different names for variables. However, these names must follow a number of syntax rules. For instance, naming a variable a result will output a syntax error because we can't use space characters in variable names.

a result = 3.98

Output
    a result = 3.98
      ^
SyntaxError: invalid syntax

These are the two syntax rules we need to follow when we're naming variables:

1. We must use only letters, numbers, or underscores (we can't use apostrophes, hyphens, spaces, etc.).
2. Variable names can't begin with a number.

Note that variable names are case sensitive, which means that a variable named result is different than a variable named Result:

result = 3.98
Result = 6.99
print(result)
print(Result)

Output
3.98
6.99

Now, let's try to correct a few variable names.

Instructions

In the code editor on the right, we attempted to store 3.5 in a variable named facebook-rating and 4.5 in a variable named instagram rating. But both of these variable names cause syntax errors, so we need to fix them.

1. Change the variable name facebook-rating to facebook_rating to prevent a syntax error.

2. Change the variable name instagram rating to instagram_rating to prevent a syntax error.

"""
facebook_rating = 3.5

instagram_rating =  4.5