"""
Programming Python Variables
1 of 6 · Saving Values
"""

""" 
Learn
In this lesson, we'll learn how to save values in Python, how to update values, and how to use syntax shortcuts to update values.

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

Let's say we want to save the result of an arithmetic operation. For example, the cost of buying Fruit Ninja Classic for two family members, 1.99 * 2 equals 3.98, and we want to save 3.98. This is the code we need to run to save 3.98:

result = 3.98

If we print the name result, the output is 3.98:
result = 3.98
print(result)

Output
3.98


We can also directly save 1.99 * 2 instead of saving 3.98.
result = 1.99 * 2
print(result)

Output
3.98

Notice, however, that print(result) outputs 3.98, not 1.99 * 2. This is because the computer first calculates 1.99 * 2 and then saves the result 3.98 to result.
"""

"""
Instructions
What is the cost of buying Minecraft: Pocket Edition for two family members?

1. Save the result of 6.99 * 2 to result.
2. Print result.
"""

result = 6.99 * 2
print(result)