# Unpacking Tuples
You can unpack tuples so you can pull different values. If you don't care about a particular value, assign it _ (basically saying do nothing with that value). Just make sure that the sizes are equal for both sides. 
```python
point = (1,2)
x,y = point

# x,y,z = point # will error since the tuple contains 2 elements, not 3
new_point = (1,2,3,4)
x,y,z,_ = new_point
a,b,c,d = new_point
print(x,y,z) # 1,2,3
print(a,b,c,d) # 1,2,3,4

```

You can also use them for dictionaries as shown below:
```python
for key,value in d.items(): # key,value is a tuple
    print(key, value)
```

