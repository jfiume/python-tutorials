from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

name = raw_input("Please type your name: ")
age = raw_input("Please type you age: ")
print "You are %s and %r years old!" % (name, age)
