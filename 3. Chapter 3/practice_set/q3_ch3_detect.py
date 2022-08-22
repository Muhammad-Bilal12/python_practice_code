

# Question 3 and 4
# Detect Double Space

str  = "this is string with  double  space"
print(str.find('  '))

str = str.replace('  ','_') # replace double space with _
print(str)


