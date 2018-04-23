#!/usr/bin/python3
# renameDates.py - Rename filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY.

import shutil
import os
import re

# Create regex that matches files with American date format.
# All text before the date.
datePattern = re.compile(r"""^(.*?)
# One or two Digits for the month
((0|1)?\d)-
# One or two digits for the day
((0|1|2|3)?\d)-
# Four digits for the year
((19|20)\d\d)
# All text after the date
(.*?)$
""", re.VERBOSE)

# Loop over the files in the working directory.
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)

    # Skyp files without a date.
    if mo == None:
        continue

    # Get the different parts of the filename.
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    # Form the European Style filename.
    euroFilename = beforePart + dayPart + '-' + \
        monthPart + '-' + yearPart + afterPart

    # Get the full, absolute file paths.
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    # Rename the files.
    print ('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))
    shutil.move(amerFilename, euroFilename)
