# Functions
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
