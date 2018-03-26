from sys import exit, argv

script, your_name = argv

def try_again():
    print "Lets look again..."
    searching1 = raw_input("Look under the seat? (Yes, No)")
    if searching1 == "yes":
        print "Amazing! You found the keys! Good job! Enjoy your new Ferrari!"
    else:
        print "I guess you don't want a free ferrari."


def ferrari_room():
    print "%s, You have found a free ferrari! Wonderful!" % your_name
    print "You only have to find the keys..."
    searching2 = raw_input("Look in the glovebox? (Yes, No)")
    if searching2 == "yes":
        print "Did not find keys. :("
        print "Look again?"
        try_again()
    elif searching2 == "no":
        print "Where should we look?"
        try_again()
    else:
        print "I guess you don't want a free ferrari."
ferrari_room()
