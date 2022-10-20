# Match statements
Match statements are new to Python but have existed in a number of different languages for a long time. Take the case from some lessons ago below:
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

Here is the alternative:
```python
number = 2
match number: # match variable
    case 1:
        print('number is 1')
    case 0:
        print('number is 0')
    case 2:
        print('number is 2')
    case number if number < 0: # matches when certain range of conditions is true
        print('number is negative')
    case number if number == 3: # can also be expressed as "case 3" since it is for a specific value but this works too
        print('number is THREE!')
    case _: # default case (the else)
        print('number is not 0, 1, 2, 3, or negative')
```
See if you can come up with other examples. Try writing them in both formats.
