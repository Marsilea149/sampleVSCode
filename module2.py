# import math
# import sys
# from os import rename

import requests

# print(sys.version)  # show the version of python
# print(sys.executable)  # show the location of python executable


def greet(who_to_greet):
    greeting = "hello, {}".format(who_to_greet)
    return greeting


r = 5

print(greet("World"))
print(greet("Bingbing"))
