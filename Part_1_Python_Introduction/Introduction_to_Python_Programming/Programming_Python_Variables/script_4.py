""" Programming Python Variables
4 of 6 · Updating Variables """

""" 
Learn
We can update the value stored in a variable. Below, we first store 1.99 in the variable app_costs, and then we update app_costs to store 6.99 instead.

app_costs = 1.99
print(app_costs)

app_costs = 6.99
print(app_costs)

Output
1.99
6.99

We can also update a variable by doing arithmetic operations:

app_costs = 1.99
print(app_costs)
print(app_costs + 6.99)

Output
1.99
8.98

Above, the variable app_costs initially stores a value of 1.99. Then, app_costs + 6.99 evaluates to 8.98 because app_costs stores a value of 1.99, so app_costs + 6.99 becomes 1.99 + 6.99. Let's look at another example:

app_costs = 1.99
app_costs = app_costs + 6.99
print(app_costs)

Output
8.98

Notice above that when we run app_costs = app_costs + 6.99, app_costs updates to store the result of app_costs + 6.99, which is 8.98. Running app_costs = app_costs + 6.99 is the same as running app_costs = 1.99 + 6.99 because app_costs stores 1.99.

Now let's practice updating variables.

Instructions

The rating count total of Fruit Ninja Classic is 698516, and the rating count total of Minecraft: Pocket Edition is 522012. Let's use these values in this exercise.

  1. Update the variable rating_count_totals by adding 522012 to its current value. 
  
  2. Print rating_count_totals.
"""
rating_count_totals = 698516 
rating_count_totals = rating_count_totals + 522012
print(rating_count_totals)