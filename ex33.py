i = 0
numbers = []

x = int(raw_input("Please type a number"))
for i in range(0, x):
    print "At the top i is %d" % i
    numbers.append(i)

    i = i + 10
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i


print "The numbers: "

for num in numbers:
    print num
