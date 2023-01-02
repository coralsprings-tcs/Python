# Functions
## None Type
None is another type of variable. It means nothing and should not confused with 0 for the sake of dicussion. It can be used as below and can even use typehints:
```python
new_var = None
other_var: None = None
print(new_var) # None
```

## Functions
Functions in Python are written as followed
```python
def function(your_paramater,your_paramter2):
    print(2+2)
def function2():
    return 'hi'
def function_true():
    return True
def match_x(item):
    if item == 'x':
        return True
    else:
        return False
```
Whenever you have a function it will automatically set the return value to None unless specified otherwise such as below:
```python
def new_func():
    print('hi')

def other_func():
    return

def another_func():
    pass

print(new_func()) # None
print(other_func()) # None
print(another_func()) # None
```

You can also typehint your parameters like below. The "-> float|int" part indicates that a value of float or int should be your output. 
```python
def adder(a:float|int, b:float|int) -> float|int:
    return a+b

adder(2.1,3) # 5.1
adder(2,3) # 5
adder(2.1,3.2) # 5.3

# If no value will be returned in a function use None for the return value typehint
def print_adder(a:float|int, b:float|int) -> None:
    print(adder(a,b))

print_adder(2.1,5.3) # 7.4

# You can also use lists as inputs or return values
def list_adder(a:[float|int], b:[int]): # a can be a list containing float values or integer values, and b can be a list that only contains integers
    pass # This is a placeholder to use for function logic

def make_new_list(a:[float]) -> [float|int]:
    # function does something with list inputs to get a list output
```
This is particularly useful when you're trying to find an error or want to know the basics of a function you are using.
