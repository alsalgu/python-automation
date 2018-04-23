#!/usr/bin/python3
# emptyFolder.py - Empties user declared folder of its contents.
# I really don't like emptying my downloads folder and I let it build up
# All due to laziness.

import os

# Main function that takes user input as folder name


def emptyFolder(folder):
    # Change directory to my home directory
    os.chdir('/home/al/')
    # Puts in the folder name to the absolute path of the dir
    folder = os.path.abspath(folder)
    # Checks to see if the full path exists.
    if os.path.exists(folder):
        # If it exists, it'll confirm this.
        print("%s exists! Checking files..." % folder)
        # And then it will loop each file in the folder to list them.
        for singleFile in os.listdir(folder):
            print(singleFile)
        # And prompt the function that confirms deletion.
        confirmDel(folder)
    else:
        # If it doesn't exist, it'll say this and re-prompt the starting
        # function.
        print("%s does not exist! Please try another!" % folder)
        return emptyFolder(input('Enter folder you wish to delete contents of: '))

# Helper function to confirm deletions.


def confirmDel(folder):
    # Saving answer as all lowercase into variable.
    answer = input('Delete Files in %s? [Y/N] ' % folder).lower()
    try:
        if answer[0] == 'y':
            # IF answer given iis yes, print path confirmation
            print('Deleting files in %s...' % os.path.abspath(folder))
            # Loop through each file in folder directory
            for singleFile in os.listdir(folder):
                # Check to see if its file or directory
                # Then remove it with appropriate command.
                if os.path.isdir(folder + '/' + singleFile):
                    print('Ignoring directory...')
                else:
                    # PRint file name.
                    print('Deleting ' + singleFile)
                    # Delete file through its full path
                    os.unlink(folder + '/' + singleFile)
            print('Done!')
        # Exit
        elif answer[0] == 'n':
            print('Goodbye!')
        # Don't accept any input besides Y/N and ask again
        else:
            print('Invalid Input')
            return confirmDel(folder)
    # Any other error just restarts this prompt
    except Exception as error:
        print("Please enter valid inputs")
        print(error)
        return confirmDel(folder)

# TODO: More error handlers, debugging, some smooth way to exit the script


emptyFolder(input('Enter folder you wish to delete contents of: '))
