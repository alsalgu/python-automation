#!/usr/bin/python3

import re

madlib = "The ADJECTIVE ADJECTIVE2 NOUN VERB over the ADJECTIVE3 NOUN2"

print(madlib)
adj = re.compile(r'ADJECTIVE\b')
madlib = adj.sub(input('Enter adjective for first noun: '), madlib)
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
if madlib == "The quick brown fox jumped over the lazy dog":
    print("I install a lot of fonts, too.")
    print(madlib)
else:
     print(madlib)
