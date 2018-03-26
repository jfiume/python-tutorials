# import modules
from sys import argv
# unpack modules
script, filename = argv
# printing
print "We're going to erase %r." %filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."
# input from user
raw_input("?")
# printing
print "Opening the file..."
# opens file
target = open(filename, 'w')
# printing
print "Truncating the file. Goodbye!"
# truncates the file, deletes all its contents
target.truncate()
# printing
print "Now I'm going to ask you for three lines."
# input recorded in variables
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")
# printing
print "I'm going to write these to the file."
# writing to the file
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
# printing
print "And finally, we close it."
# closing the file
target.close()
