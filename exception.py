import sys
class PositiveInvalid(Exception):
    pass
class NegativeInvalid(Exception):
    pass
try:
    print("Enter the marks:")
    marks=int(input())
    if marks<0:
        raise NegativeInvalid
    if marks>100:
        raise PositiveInvalid
except NegativeInvalid:
    print("Negative Out of Range",sys.exc_info())
except PositiveInvalid:
    print("Positive out of range",sys.exc_info())