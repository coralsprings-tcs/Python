# Variables
The basic variable types are:
* string
* integer
* float / decimal
* boolean
You should note there are others but they are not important to here.

## Examples
```python
a = 'a string' # This is a string
b = "5" # This is also a string
b2 = '''5'''
c = '''
This is a multiline string.
It can be one or more lines.
You have to use triple quotes for this to work.
For single line strings you can use single, double or triple quotes.
'''
d = 5 # this is an int
e = 9.2 # this is a float (decimal)
g = True # this is a boolean
h = False # this is also a boolean
```

# Duck / Dynamic Typing
You can do the following thanks to it:
```python
a = 5
b = 5.5
print(a+b) # print literally prints to screen
```
Python figures out based on variable "b" that "a" should be a float value. This is a lot different than Java, C, and other static type languages.
```c
float a = 5;
// doing int a = 5 will cause the compiler to complain so will not work
float b = 5.5;
printf(a+b)
```
If it walks like a duck, quacks like a duck, it is a duck. This is how Python figures out what to do with variables. If it looks like a string, acts like a string, it is a string. No declaration needed for most cases. Sometimes, though, it will not work like with below. Try it out!
```python
print(5+'things')
```

Last thing to try is the below:
```python
str_input = input('Enter an input:' ) # What you put in is an input
print(str_input)
```

# Review
* What happens when you try print(5+'string')?
* When you try print(5+5)?
* Why?


