# unpack modules
from sys import argv
# define modules
script, intput_file = argv
# function that prints f
def print_all(f):
    print f.read()
# function that sets f to 0
def rewind(f):
    f.seek(0)
# function that prints 1 line of f
def print_a_line(line_count, f):
    print line_count, f.readline()
# sets the input file to the currnet file
current_file = open(intput_file)
# prints
print "First let's print the whole file:\n"
# calls the print_all function on the current file
print_all(current_file)
# prints
print "Now let's rewind, kind of like a tape."
# calls the rewind fucntion on the current file
rewind(current_file)
# prints
print "Let's print three lines:"
# sets the current line to 1
current_line = 1
# calls the print a line function on the current file and the active line
print_a_line(current_line, current_file)
# 1st it increments the current line. then it calls the print a line function on the current file and the active line
current_line = current_line + 1
print_a_line(current_line, current_file)
# 1st it increments the current line. then it calls the print a line function on the current file and the active line
current_line = current_line + 1
print_a_line(current_line, current_file)
