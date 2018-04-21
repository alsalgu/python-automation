#!/usr/bin/python3

import re

# Store mad lib story in variable for easy access
madlib = "The ADJECTIVE ADJECTIVE2 NOUN VERB over the ADJECTIVE3 NOUN2"
# Print mad lib in terminal for reference
print(madlib)
# Regular expression to find word to replace
adj = re.compile(r'ADJECTIVE\b')
# Substitute the regex to subsitute it with user input in the madlib string.
# Save it in the madlib variable
madlib = adj.sub(input('Enter adjective for first noun: '), madlib)
# Repeat of the process above but for different word searches
adj2 = re.compile(r'ADJECTIVE2')
madlib = adj2.sub(input('Enter second adjective for first noun: '), madlib)
noun = re.compile(r'NOUN\b')
madlib = noun.sub(input('Enter first noun: '), madlib)
verb = re.compile(r'VERB')
madlib = verb.sub(input('Enter verb for first noun: '), madlib)
adj3 = re.compile(r'ADJECTIVE3')
madlib = adj3.sub(input('Enter first adjective for second noun: '), madlib)
noun2 = re.compile(r'NOUN2')
madlib = noun2.sub(input('Enter second noun: '), madlib)
# Check if user-input-string matches this one
# Print the madlib and a 'joke'
if madlib == "The quick brown fox jumped over the lazy dog":
    print("I install a lot of fonts, too.")
    print(madlib)
# If not, just print the madlib
else:
    print(madlib)
