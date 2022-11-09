# Dictionaries
Dictionaries have keys and values like how dictionary books have words and their definitions. Unlike the book kind though you can only have one value per key, however the value can be anything (even a list or other collection). We will revisit this topic since this can be more technical. They are very useful in Python for a wide number of cases.
```python
items = {}
items['a'] = 1 # Define key "a" and assign 1 to it
items['a'] = 'new' # This is how you can update a value in a dictionary
new_items = {'b':'xyz','c':12345,'d':[1,2,3,4],'e':{'1':2,'f':'last'}}

# To remove you can do the following:
del new_items['b']
new_items.pop('c')
# Try finding the difference between the methods by using Python in a console!
```

You can cycle through the keys of the dictionary or the values as well:
```python
new_items = {'b':'xyz','c':12345,'d':[1,2,3,4],'e':{'1':2,'f':'last'}}
# Getting the keys
for key in new_items.keys():
    print(key)

# Getting the values
for key in new_items.keys():
    print(new_items[key])

for value in new_items.values():
    print(value)

# Getting both
for key in new_items.keys():
    print(key, new_items[key])
```
