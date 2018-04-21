#!/usr/bin/python3
# Pattern matching in python

import pyperclip
import re

# Phone Regular Expression, triple ' allows muliple lines
phoneRegex = re.compile(r'''(
# Area Code with three digits, Optional (followed by ?)
# Pipe Match two possible ways to write it.
(\d{3}|\(\d{3}\))?
# Seperator, space or hyphen or period. Optional.
(\s|-|\.)?
# Three more digits.
(\d{3})
# Another seperator, space or hyphen or period.
(\s|-|\.)
# Four More Digits
(\d{4})
# Space, multiple ext, space, 2 or five digis. Optional
(\s*(ext|x|ext.)\s*(\d{2,5}))?
)''', re.VERBOSE)

# Create email regex.
emailRegex = re.compile(r'''(
# Username, lower/uppercase alphabet, numbers, symbols
[a-zA-Z0-9._%+-]+
# Plus at symbol
@ +
# Plus more acceptable digits/letters
[a-zA-Z0-9.-] +
# Plus a dot and 2 or 4 acceptable letters
(\.[a-zA-z]{2,4})
)''', re.VERBOSE)

# Find matches in clipboard text.
# Collect clipboard and save it into a variable
text = str(pyperclip.paste())
# Empty List variable
matches = []
# Iterate all groups found in the clipboard search of each function
# Then append it to the matchest list variable
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Copy the results to the clipboard.
# If length of matches has anything in it
# Copy the matches list into the clipboard
# Then print in terminal that it was done, plus the matches
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
