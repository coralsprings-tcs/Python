# List comprehension
List comprehension is an easier way to write lists. Compare the below and see what is easier for yourself. The best way to explain them is show them and see how they compare after all.
```python
# For loop
for i in items:
    print(i)
# List comprehension
[print(i) for i in items]

# For loop
for i in new_items:
    if i == 'item':
        print('item')
    else:
        print('not item')
[print('item') if i=='x' else print('not item') for i in new_items]

```
