# variables
The basic variable types are:
* string
* integer
* float / decimal
* boolean
You should note there are others but they can be more advanced.

```python
a = 'a string' # This is a string
b = "5" # This is also a string
c = '''
This is a multiline string.
It can be one or more lines.
You have to use triple quotes for this.
For single line comments you can use single, double or triple quotes.
'''
d = 5 # this is an int
e = 9.2 # this is a float (decimal)
g = True # this is a boolean
h = False # this is also a boolean
```
You can convert one item to another using conversions like the following. We will come back to this because it leads to a very useful trick.
```python
test_item = 5
str(test_item)
int(test_item)
float(test_item)
bool(test_item)
```

# Duck / Dynamic Typing
You can do the following thanks to it:
```python
a = 5
b = 5.5
print(a+b)
```
Python figures out based on variable "b" that "a" should be a float value. This is a lot different than Java, C, and other static type languages.
```c
float a = 5;
// doing int a = 5 will cause the compiler to complain
float b = 5.5;
printf(a+b)
```

# Lists
Lists are not exactly arrays. Doing arrays in Python is a bit complicated so we will come back to them. Doing lists is much easier. It is important to know that the index starts with 0 (not 1 as you would in a regular list). You can get any value in a list by doing list[index] where list is the name of your list and index is any whole number.
```python
items = ['st', 5, False, 3.14] # list has string, int, boolean, and float in that order
print(items[0]) # st, the first item
print(items[1]) # 5, the second item

print(items[-1]) # 3.14, the last item / first from the right
print(items[-2]) # False, second item from the right

items.pop(1) # This will remove the second item (index = 1) from the list
items.append('new item') # This will add an item to the end of the list
items.insert(0, 'newer') # newer will be put at index = 0 (first list item)
items[2] = 100 # This will replace the third (index=2) item 
print(items) # ['newer', 'st', 100, 3.14, 'new item']
print(len(items)) # how you get how many items in the list, also known as the length
# For len(items), you will get 5
```

# Tuples
Tuples are like lists in that they are ways to collect items, however they are immutable (meaning can't be changed).
```python
items = (1,2,3,4)
# items.pop(0) # Doing this will fail. Try uncommenting it to see the error.
print(items[1]) # 2
print(items[-1]) # 4
```

# Dictionaries
Dictionaries have keys and values like how dictionary books have words and their definitions. Unlike the book kind though you can only have one value per key, however the value can be anything (even a list or other collection). We will revisit this topic since this can be more technical.
```python
items = {}
items['a'] = 1 # Define key "a" and assign 1 to it
new_items = {'b':'xyz','c':12345,'d':[1,2,3,4],'e':{'1':2,'f':'last'}}
```

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

# Loops
Loops are pretty basic in Python for the most part.
## For
```python
items = [1,2,3,4,5]
# print(item) # calling this here will give an error
for item in items:
    print(item)

print(item) # 5 because that is the last item in list
```
Try explaining why this works the way it does and you got for loops. Compare this to doing a similar loop in C!
```c
items = {1,2,3,4,5}
// Below you start with index 0 and loop through all items in the length
// As you can see, you have to hardcode the endpoint
for (i = 0; i < 5; ++i) 
{
    printf("%d ", items[i]);
}
```
## While
Python does not have do-while loops that are common to other languages (if you don't know what they are, don't worry about it as it isn't relevant here).
```python
while True:
    # do thing
```
An example is:
```python
i = 0
while i <= 5: # while i is less than or equal to 5
    print(i)
    i += 1 # i = i + 1
```
Bringing if/thens and while loops together:
```python
i = 0
while True:
    print(i)
    if i < 6:
        i += 1
    else:
        break
```

# One More Thing
## Typehints
You can give variables typehint for debugging and telling people using your code what type of variable you are expecting.
```python
a: float = 5
# using a: int = 5 will NOT cause Python to complain
b: float = 5.5
print(a+b)
```

## Useful Boolean Stuff
F-strings are super useful in putting different variable types in the same statement or just giving a string for printing.
```python
item_amnt = 5
print(f'There are {item_amnt} items') # f-string used here to print item_amnt in the same string as the other text
```
Look them up here: https://realpython.com/python-f-strings/#:~:text=Also%20called%20“formatted%20string%20literals,the%20__format__%20protocol.

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
To put it another way will you get true or false with the following (check below it for answers)?
```python
bool(5) # Question 1
bool(0) # Question 2
bool(-5) # Question 3
```


The answers to the above questions are:

>! Question 1 - True

>! Question 2 - False

>! Question 3 - True

The same applies with float values. If you put in bool(float(0)) you will get False. For any other float number you will get True. This is because of how Python works. All the below will give you true:
```python
bool(5.5) # bool(float)
bool(-21.1) # bool(float)
bool(21) # bool(int)
bool(1) # bool(int)
bool('this is a string') # bool(str)
```
And the below will give you false:
```python
bool(0)
bool(float(0))
bool('')
```
