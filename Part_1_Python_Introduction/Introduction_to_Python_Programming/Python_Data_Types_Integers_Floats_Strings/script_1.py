""" Python Data Types: Integers, Floats, Strings
1 of 8 · Integers and Floats"""

"""
Learn
In this lesson, we'll learn about data types in Python: integers, floats, and strings.

Throughout this lesson, we'll learn core Python programming concepts in the context of real data. We'll be using data from the table below, which provides some information about five mobile applications from the iOS store:

track_name	| price	| currency|rating_count_tot	 | user_rating
Facebook	     0.0	    USD	      2974676	            3.5

Instagram	      0.0	    USD	      2161558	            4.5

Clash of 
Clans	          0.0 	  USD	      2130805	            4.5

Fruit Ninja 
Classic         1.99	  USD	      698516	            4.5

Minecraft:
Pocket Edition	6.99	  USD	       522012	            4.5

In Python, we can make computations with integers (like 1) and decimal numbers (like 6.99):

print(6.99 * 1)
print(0.0 + 1.99)

Output
6.99
1.99

In mathematics, integers aren't the same as decimal numbers, and Python acknowledges this difference. We can use the type() function to see the type of a value and confirm that Python distinguishes between integers and decimal numbers:

print(type(0))

print(type(0.0))

Output
int
float

Notice that the integer 0 has the int type and the decimal number 0.0 has the float type. All integers have the int type, and all decimal numbers have the float type.

In computer programming, we classify values into different types — or data types. The type of value offers the computer the required information about how to process that value. Depending on the type, the computer will know how to store a value in memory, or what operations we can and can't perform on a value.

int and float values have different types, but we can mix the values together in arithmetical operations. So we're not limited, for instance, to adding an int value only to another int value — we can add an int value to a float value:

print(0 + 6.99)
print(1.99 * 2)

Output 
6.99
3.98

Instructions

For these exercises, practice mixing float and integer numbers to update variables. Suppose that you're tracking the cost of app purchases for personal use, and the cost of app purchases as gifts to friends.

1.Create a variable to record personal app store purchases, and update the variable to reflect purchasing Fruit Ninja Classic.
  . Initiate the variable personal_apps by assigning the integer value of 0.
  . Update the value of personal_apps by adding the float 1.99 to its current value.
  . You can use the += operator.
  
2. Record the app cost for Minecraft: Pocket Edition, and update the variable to reflect purchasing it for three friends.

  . Assign the float 6.99 to a variable named gift_apps.
  . Update the value of gift_apps by multiplying its current value by the integer 3.
  . You can use the *= operator.
  
3. Display personal_apps and gift_apps using print().
"""

personal_apps = 0

personal_apps += 1.99

gift_apps = 6.99

gift_apps *= 3

print(personal_apps)
print(gift_apps)