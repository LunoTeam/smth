

from sys import argv
script, filename = argv

print "Hey, we are gonna erase %r." % filename
print "If you don't wanna do that hit ctrl+c"
print "If you do want, hit return"

raw_input("?")

print "Opening the file"
target = open(filename, 'w')

print "Truncating the file. Good bye!"
target.truncate()

print "Now I'm going to ask you for three lines"
line1 = raw_input("Line1: ")
line2 = raw_input("Line2: ")
line3 = raw_input("Line3: ")


print "I'm going to write these to the file"
target.write(line1)
target.write("/n")
target.write(line2)
target.write("/n")
target.write(line3)
target.write("/n")


print "And finally we close it"
target.close
