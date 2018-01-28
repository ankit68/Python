#!/usr/bin/python3

a,b=0,1
if a>b:
    print ("value of a ({}) is less than b ({})".format(a,b))
else:
    print("value of a ({}) is not less than  b ({})".format(a,b))

print ("foo" if a < b else "bar")
