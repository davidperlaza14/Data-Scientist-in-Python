""" 
Programming Python Variables
2 of 6 · Variables
"""
""" 
Learn
Earlier, in the learn section of the previous screen, we saved 3.98 to result.

result = 3.98

When we run the code result = 3.98, the value 3.98 gets saved in the computer memory. The computer memory has many storage locations, and 3.98 gets saved to one particular location.

The storage location where we saved 3.98 has a unique identifier, and we can use it to access 3.98. The name of the identifier is result; we named it that way when we ran the code result = 3.98. We can use the identifier result to access 3.98 in other lines of code:

result = 3.98
print(result)
print(result + 1.99)

Output
3.98
5.97

The storage location for 3.98 is a variable. When we ran the code result = 3.98, we stored 3.98 in a variable (storage location) named result, so result is a variable name.

Note that we need to write the variable name to the left of the = operator and the value we want to store to the right. So if we want to store the value 3.98 to a variable named result, we must write result = 3.98, not 3.98 = result.

We chose the name result arbitrarily, but we could have chosen something different:

fruit_ninjas = 3.98
print(fruit_ninjas)
print(fruit_ninjas + 1.99)

Output
3.98
5.97

Now let's practice using variables.

Instructions

1. Store the value 6.99 in a variable named minecraft_cost.

2. Store the result of 1.99 * 1 to a variable named fruit_ninja_cost.

3. Using the print() function, display the following:

  .The value stored in the minecraft_cost variable.
  
  .The result of adding 1.99 to the variable fruit_ninja_cost.
  
  .The result of adding fruit_ninja_cost to minecraft_cost.
"""

minecraft_cost = 6.99

fruit_ninja_cost = 1.99 * 1

print(minecraft_cost)

print(fruit_ninja_cost + 1.99)

print(minecraft_cost + fruit_ninja_cost)