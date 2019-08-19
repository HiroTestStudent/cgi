#!/usr/bin/env python
import cgi

print("Content_Type: text/plain")
print("")

form = cgi.FieldStorage()
stringval = form.getvalue('a', None)
listval = form.getlist('b')

print("a: {}, b: {}".format(str(stringval), str(listval)))

