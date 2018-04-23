#!/usr/bin/python3
# mcb.pyw - Saves and loads pieces of text to clipboard.
# Usage:
# python3 mcb.pyw save <keyword> - Saves clipboard to keyword.
# python3 mcb.pyw <keyword> - Loads keyword to clipboard.
# python3 mcb.pyw list - Loads all keywoards to clipboard.
# python3 mcb.pyw delete <keyword> - Deletes saved keyword.
# python3 mcb.pyw deleteAll - Deletes all keywords.

import shelve
import pyperclip
import sys

# Shelf file name that will open to store/load clipboards
mcbShelf = shelve.open('mcb')

# Save clipboard content.
# If there are 3 command arguments and the one at index 1 is the word Save
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    # mcbShelf will use the argument at index 2 as a variable to store
    # what is in the clipboard.
    mcbShelf[sys.argv[2]] = pyperclip.paste()
# If there are 3 command arguments and the one at index 1 is the word Delete
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    # Delete the shelf that matches the word at index 2
    del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2:
    # List keywords and load content.
    # If the argument at index 1 is the word list
    if sys.argv[1].lower() == 'list':
        # The clipboard will copy a string representation of a list of keys
        # from the shelf
        pyperclip.copy(str(list(mcbShelf.keys())))
    # If the argument at index 1 is the word deleteAll
    elif sys.argv[1].lower() == 'deleteAll':
        # Clear the entire list.
        mcbShelf.clear()
    # Else if the argument at index 1 is in the actual shelf
    elif sys.argv[1] in mcbShelf:
        # Copy what is stored in that shelf value into the clipboard
        pyperclip.copy(mcbShelf[sys.argv[1]])


mcbShelf.close()
