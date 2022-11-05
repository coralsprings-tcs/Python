## F-strings
F-strings are super useful in putting different variable types in the same statement or just giving a string for printing.
```python
item_amnt = 5
print(f'There are {item_amnt} items') # f-string used here to print item_amnt in the same string as the other text

new_str = f'There are {item_amnt} lights' # You can store an f-string as a variable
print(new_str)

obj_amnt = 6
obj_name = 'Pokemon'
obj_str = f'You can only carry {obj_amnt} {obj_name}.' # You can store any number of variables in a f-string
print(obj_str) # 'You can only carry 6 Pokemon.'
```
Look them up here: https://realpython.com/python-f-strings/#:~:text=Also%20called%20“formatted%20string%20literals,the%20__format__%20protocol.

# Review
* Can you store an f-string as a variable?
* What type of variable does an f-string return? (ie. boolean, string, int)
* What are the escape characters for f-string? How do you get around them?
