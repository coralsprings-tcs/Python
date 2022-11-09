# Try-except-else-finally is a way of handling exceptions/errors that can occur with Python.
# If you know try-catch in other languages, you'll do fine. 
# If not, they are not too hard in Python.
# try:
    # code that may fail
# except Exception (of a particular type): 
# or except (will work for all exceptions):
    # For 1+ exceptions
# else:
    # if what happened in try works, do this
# finally:
    # does whether or not exception occurs
# The else and finally are optional.

# An example is below:
try:
    print(1+'s')
except:
    print('An error occured')

print()
# For more specific cases you can do below:
try:
    print(1+'s')
except TypeError:
    print("Can't match a string and an int together!")
