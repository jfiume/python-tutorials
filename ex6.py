# x is a string that says there are 10 types of people
x = "There are %d types of people" % 10
# variable defining binary
binary = "binary"
# variable defining don't
do_not = "don't"
# y is a string with binary and don't
y = "Those who know %s and those who %s." % (binary, do_not)

# printing strings
print x
print y

#printing the same strings with a phrase in front
print "I said: %r." %x
print "I also said: '%s'." %y

# define boolean variable
hilarious = False
#string variable
joke_evaluation = "Isn't that joke so funny?! %r"

# prints string with a variable in it
print joke_evaluation % hilarious

# one string
w = "This is the left side of..."
# another string
e = "a string with a right side."

#prints a concatanation of a string
print w + e
