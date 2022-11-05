# Typehints
You can give variables typehint for debugging and telling people using your code what type of variable you are expecting. Can you think of why Python works this way?
```python
a: float = 5
# using a: int = 5 will NOT cause Python to complain
b: float = 5.5
print(a+b)

# use the pipe operator (|) when you want to say it can be either of two or more types
c: float|int = 10 
d: float|int|str = '10'
```

# Review
* Do the typehints need to match the actual variable type?
* How do you set multiple typehints for a single variable?
