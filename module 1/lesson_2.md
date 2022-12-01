# Lists
Lists are not exactly arrays. Doing arrays in Python is a bit complicated so we will come back to them. Doing lists is much easier. It is important to know that the index starts with 0 (not 1 as you would in an everyday list). You can get any value in a list by doing list[index] where list is the name of your list and index is any whole number.
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

Lists can have lists in them so 
```python
list_of_lists = [[1,2,3,4],[5,6,7],['a','b','c']]
```
will work in Python.
