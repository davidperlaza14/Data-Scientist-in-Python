""" 
Python Data Types: Integers, Floats, Strings
2 of 8 · Conversion Between Types
"""

""" 
Learn
It's possible to convert a float to an integer — and vice versa. To convert an integer to a float, we can use the float() function:

print(float(0))

Output
0.0

To convert a float to an integer, we can use the int() function:

print(int(1.99))

Output
1

Notice the int() function rounded 1.99 down to 1. int() will always round a float down, even if the number after the decimal point is greater than five.

print(int(6.99))

Output 6

If we want to round off a number, we can instead use the round() function, which has more flexibility and can also round up:

print(round(6.99))

print(round(1.99))

print(round(0.0))

Output
7
2
0

Notice that it's possible to combine functions. For instance, we encompassed a round() function within a print() function in each of the examples above.

Note that running the round() function doesn't change the value stored by a variable unless we assign the rounded value back to the variable:


minecraft_cost = 6.99
print(round(minecraft_cost))
print(minecraft_cost)

minecraft_cost = round(minecraft_cost)
print(minecraft_cost)

Output
7
6.99
7

Let's practice.

Instructions

To complete this exercise, add your code on a new line below the provided code. Do not modify the existing code.

1. Round personal_apps using the round() function, and assign the rounded value back to personal_apps.

2. Convert gift_apps from a float to an integer using the int() function, and assign the converted value back to gift_apps.

3. Display personal_apps and gift_apps using the print() function.
"""

personal_apps = 0
personal_apps += 1.99

gift_apps = 6.99
gift_apps *= 3 

print(personal_apps)
print(gift_apps)

# Update the values of personal_apps and gift_apps
# Write your code below this line

personal_apps = round(personal_apps)
print(personal_apps)

gift_apps = int(gift_apps)
print(gift_apps)