# unpacks the module
from sys import argv
# defines what varibles to unpack.
script, filename = argv
# sets a variable name to the file to open
txt = open(filename)
# shows the name of the file
print "Here's your file %r" % filename
# prints the contents of the file
print txt.read()
close(filename)
# prompt input
print "Type the filename again:"
file_again = raw_input(">")
# defines the file name again
txt_again = open(file_again)
# prints the contents of the file
print txt_again.read()
close(file_again)
