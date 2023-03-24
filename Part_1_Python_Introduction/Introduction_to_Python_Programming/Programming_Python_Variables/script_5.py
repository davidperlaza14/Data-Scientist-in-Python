""" Programming Python Variables
5 of 6 · Syntax Shortcuts"""

""" 
Learn
On the previous screen, we used the code app_costs = app_costs + 6.99 to update app_costs from 1.99 to 8.98.

app_costs = 1.99
print(app_costs)
print(app_costs + 6.99)

app_costs = app_costs + 6.99
print(app_costs)

Output
1.99
8.98
8.98

There are several syntax shortcuts we can use to update a variable when we're doing arithmetic operations. For example, as an alternative to the code above, we can write app_costs += 6.99 (instead of app_costs = app_costs + 6.99):

app_costs = 1.99
app_costs += 6.99
print(app_costs)

Output
8.98



Note that we can only use these operators (+=, -=, *=, /=, **=) to update a variable. This means the variable we're updating must already store a value. In other words, the variable must already be defined. When we try to update a variable that we haven't defined, we get an error called NameError.

"""
rating_count_totals = 698516

rating_count_totals += 522012

fruit_ninja_totals = 1.99

fruit_ninja_totals *= 4

print(rating_count_totals)
print(fruit_ninja_totals)