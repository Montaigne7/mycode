#!/usr/bin/env python3

# Lists for manipulating with append and extend methods
proto = ["ssh", "http", "https"]
protoa = ["ssh", "http", "https"]
proto2 = [ 22, 80, 443, 53 ]

# append a list into another and display to screen
proto.append(proto2)
print(proto)

# extend a list into another and display to screen
protoa.extend(proto2)
print(protoa)

