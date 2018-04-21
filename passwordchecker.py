#!/usr/bin/python3

import re

# Password Checker in Terminal
# Stores User Input in Variable
password = input('Enter Password you wanna check: ')
# Requirements for Password, 8 characters min, one digit, one symbol, one cap
passRegex = re.compile(r'''(
((?=.*[\d])(?=.*[A-Z])(?=.*[a-z])(?=.*[!@#$])[\w\d!@#$]{8,}$)
)''', re.VERBOSE)
# Passes input variable into search all function
result = passRegex.findall(password)
# If input has results or lacks it confirm it
if len(result) > 0:
    print('Your password meets all requirements!')
else:
    print('Your password needs all of the following: 8 digits, 1 Cap, 1 Number, 1 Symbol')
