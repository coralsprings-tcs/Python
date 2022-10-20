# If / Else
```python
if True:
    print('true condition')
else:
    print('false condition')
```
A cheesy example is:
```python
condition = 'No cookies'
if (condition == 'I get cookies'): # If the condition given is 'I get cookies'
    print('Yay cookies')
else: # Anything other than 'I get cookies' for condition
    print('I get cake')
```
We can also write:
```python
number = 5:
if not number < 5:
    print('number is greater than or equal to 5')
else:
    print('number is less than 5')
```
OR
```python
number = 5:
if number < 5:
    print('number is less than 5')
else:
    print('number is greater than or equal to 5')
```
You can also add an elif, which means else-if. It is shown below:
```python
number = 0:
if number > 0:
    print('number is positive')
elif number == 0:
    print('number is zero')
else:
    print('number is negative')
```
You can have more than one elif in the same if-else sequence (you can't have more than 1 if, hence why).
```python
number = 2:
if number == 1:
    print('number is 1')
elif number == 0:
    print('number is 0')
elif number == 2:
    print('number is 2')
elif number == 3:
    print('number is 3')
elif number < 0:
    print('number is negative')
else:
    print('number is not 0, 1, 2, 3, or negative')
```

Think about how messy this can get with enough conditions. A later lesson will be an alternative release in Python 3.10 (a few years ago).
