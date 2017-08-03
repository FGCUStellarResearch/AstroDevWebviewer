#!/usr/bin/env python
"""
    AstroDevWebviewer python

"""

# TODO: imports
import cgitb
cgitb.enable(display=0, logdir="./")

print 'Content-type:text/html\r\n\r\n'
print '<!DOCTYPE html>\r\n <html lang="en"> \r\n'

# TODO: make this printing out a function that takes the file as an input
with open("./header.html") as header:
    for line in header:
        print line
with open("./index.html") as htmlfile:
    for line in htmlfile:
        print line
with open("./footer.html") as footer:
    for line in footer:
        print line

print "</html>"


