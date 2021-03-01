# Creating simple description (aka documentation)
def my_function(x):
  '''This function returns a doubled value of its arguments''' 
  return x*2
print(my_function(15))

# To print the description:
print(my_function.__doc__)
