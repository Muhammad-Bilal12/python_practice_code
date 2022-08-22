

# let's try some String Function



str = 'this is String'
print(len(str)) # find length  of String


str = '''
learn Python One Video in Hindi: 
This Python Programming in Hindi tutorial is a complete python course in Hindi comprising
 of 13 Python chapters and 3 Python Projects.
  After watching this course you can learn Python programming easily in Hindi. 
  This Python programming course for beginners in Hindi is designed keeping in mind the current 
  trend and recent changes in Python. 
  This course is designed to teach Python to beginners making it one of the best
   sources to learn python in Hindi for beginners.
    Get ready to learn python programming in a fun way and make sure
     to download the python notes which are included with this video.
      Hope you enjoy this course on python programming for beginners in Hindi.
'''


# check= str.endswith('hindi') #check wheter the word ends with given word or not
# and return boolean values
# print(check)


# check = str.count('python') # check how many times python appear on this text and return int value

# print(check)

# print(str.lower()) #lower case
# print(str.capitalize()) #capitaalize case
# print(str.upper()) #uppercase

check = str.find('python')

# print(check) # return first idex of finding word 
# if word is more than one time it gives only first appereance in this string

# Rewrite our string with replacing word python to html
str = str.replace('Python','Html')
print(str)


# just check it out this topics
