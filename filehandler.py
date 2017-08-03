#!/usr/bin/env python
"""
    AstroDevWebviewer python

"""

# TODO: imports
import cgi
import os
import sys
import cgitb
cgitb.enable(display=0, logdir="./")

message = "Hello Central!"
form = cgi.FieldStorage()


try:
    # Get filename
    fileitem = form.getvalue('filename')
    
    if fileitem:
        message = 'The file uploaded successfully\n\n'

        open('./tmp/' + 'tryit.csv', 'wb').write(fileitem)    
    
    else:
        message = 'No file was uploaded'
except Exception as e:
    message = 'Error with form: ' + str(e)

print 'Content-type:text/html\r\n\r\n'
print '<!DOCTYPE html>\r\n <html lang="en"> \r\n'


with open("./header.html") as header:
    for line in header:
        print line

print '<div></div><p>' + message + '</p><div></div>'

with open("./firsthalf.html") as header:
    for line in header:
        print line

with open("./footer.html") as footer:
    for line in footer:
        print line

print '</html>'


