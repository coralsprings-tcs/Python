# Boolean conversion
You can also do the following in Python:
```python
u = True + 1
w = int(True)
x = float(False)
y = bool('this is a string')
z = bool('')
```

The question there becomes why. See if you can find why after looking at the below (note that != means "not equal to"):
```python
items = [] # a list with zero items in it, so len(items) will be 0
if len(items): # can also write as "if len(items) != 0:" which means length of items is not equal to zero
    print('Items list has values')
else: # what happens if length of items is zero
    print('List has no values')
```
To put it another way will you get true or false with the following (check the next part for answers)?
```python
bool(5) # Question 1
bool(0) # Question 2
bool(-5) # Question 3
```
