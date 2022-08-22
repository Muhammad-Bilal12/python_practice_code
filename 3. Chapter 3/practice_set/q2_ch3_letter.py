

letter = '''
Dear <|NAME|>
\tYou are selected

Date : <|DATE|>

'''
name = input('Enter Your Name : ')
date = input('Enter your date : ')

letter = letter.replace('<|NAME|>',name)
letter = letter.replace('<|DATE|>',date)

print(letter)