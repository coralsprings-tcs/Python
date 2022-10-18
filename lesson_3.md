# None Type
There is another type of simple variable that is analogous to nil, null, etc. This is not to be confused with zero as they are different things in computer speak.
```python
a_thing = None
print(None + 1) # Will fail because different types are trying to be added
```

NOTE: The boolean for None is False so the following will work:
```python
result = None
if result:
    print('You got a result')
else:
    print('No result found') # What you will get since result = None
```

# Functions
Functions are pretty simple to define.
```python
def thing():
# Telling Python I am making a function by using def as a keyword
    # and calling the function thing with no parameters/inputs
    return 'x' # 'x' is your output

result = thing() # calling the function and storing to a vairable called result
print(result) # x

def new_thing(anything):
    return str(anything) # returns a string variable

result = new_thing(5)
result_two = new_thing('test')
print(result) # '5'
print(result_two) # 'test'

def other_thing(item_one, item_two)
    return f'{item_one}{item_two}' # this can take inputs of any type so it doesn't error
print(other_thing(1,'test')) # 1test
print(other_thing(1, 2)) # 3
print(other_thing('test','ing')) # testing

def newer_thing(param1,param2,param3):
    print(f'{param1}{param2}{param3}')
    # this will return None since there is no return defined
newer_thing(1,2,3) # 123
newer_thing('a','b','c') # abc
print(newer_thing('1','2','3')) # None
```



# One More Thing
There two things you might find helpful for computer science speak and as good habits to start with.
## Guard Clauses
Guard clauses are useful for covering edge cases, especially when having certain parameters can cause an error (remember Python has dynamic typing so does not check types from the beginning).
```python
def expensive_function(param_list):
    if len(param_list) == 0: # if len of the list paramter is zero
        raise ValueError('List is empty')
    # logic that has a high memory cost
    return param_list[1]
```

## Typehinted Functions
You can use typehints for functions. Python does not check parameter or value types but it is useful for debugging and figuring out what a function does.
```python
def new_thing(a:int|str, b:str) -> None:
# a should be an int or str, b should be a str
# will return a None type
    print(f'{a} {b}')

def subtract(a:int,b:int) -> int:
# will return an int using two integer parameters 
    return a-b
```
