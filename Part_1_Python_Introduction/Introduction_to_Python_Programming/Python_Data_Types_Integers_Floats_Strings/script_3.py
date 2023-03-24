""" 
Python Data Types: Integers, Floats, Strings
3 of 8 · Strings 
"""

""" 
Learn
So far, we've only worked with int and float values. But in data science, numbers aren't the only type of data we work with. Let's refer once again to our dataset about five mobile applications from the iOS store:

track_name	| price	| currency|rating_count_tot	 | user_rating
Facebook	     0.0	    USD	      2974676	            3.5

Instagram	      0.0	    USD	      2161558	            4.5

Clash of 
Clans	          0.0 	  USD	      2130805	            4.5

Fruit Ninja 
Classic         1.99	  USD	      698516	            4.5

Minecraft:
Pocket Edition	6.99	  USD	       522012	            4.5

We can see that text (not numbers) represents the data in columns track_name and currency. In Python, we can create text by enclosing a sequence of characters within quotation marks (" "):

app_name = "Facebook"
currency = "USD"

print(app_name)
print(currency)

Output
Facebook
USD


Python syntax allows both double quotation marks (" ") and single quotation marks (' '). So, if we want to create the word "Facebook," we can use either "Facebook", or 'Facebook'.

fb_1 = "Facebook"
fb_2 = 'Facebook'

print(fb_1)
print(fb_2)

Output
Facebook
Facebook

In programming, we call sequences of characters like "Facebook", "USD", or "dasdaslkj" strings. In Python, a string is of the str type:

print(type('Facebook'))

Output
str

When we create strings, we can also use numbers, spaces, or other characters:

game = 'Clash of Clans'
short_description = 'Clash of Clans is free and has an average rating of 4.5'

print(game)
print(short_description)

Output
Clash of Clans
Clash of Clans is free and has an average rating of 4.5

"""

""" 
Instructions
Assign the string Minecraft: Pocket Edition to a variable named app_name.
Assign the string 4.5 to a variable named average_rating. Don't mistake a string for a float.
Assign the string 522012 to a variable named total_ratings. Don't mistake a string for an integer.
Display the app_name variable using print().
"""

app_name = " Minecraft: Pocket Edition"

average_rating = "4.5"

total_ratings = "522012"

print(app_name)