# Output Variables
# The Python print() function is often used to output variables.

x = "Hello World"
print(x)


# In the print() function, you output multiple variables, separated by a comma.

a = "Python"
b = " is a"
c = " Programming language"

print(a,b,c)


# You can also use the + operator to output multiple variables:

m = "Hi"
n = " I am good"
p = " and you"

print(m + n + p)


# For numbers, the + character works as a mathematical operator:

x = 5
y = 10
print(x + y)

# In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:
# The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:

x = 5
y = "John"
##print(x + y)
print(x, y)


