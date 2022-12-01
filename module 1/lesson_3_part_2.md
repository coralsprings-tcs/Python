# Loops
Loops are pretty basic in Python for the most part.
## For
```python
items = [1,2,3,4,5]
# print(item) # calling this here will give an error
for item in items:
    print(item)
else:
    # optional to put an else but can be used for any loop

print(item) # 5 because that is the last item in list
```
Try explaining why this works the way it does and you got for loops. Compare this to doing a similar loop in C.
```c
items = {1,2,3,4,5}
// Below you start with index 0 and loop through all items in the length
// As you can see, you have to hardcode the endpoint
for (i = 0; i < 5; ++i) 
{
    printf("%d ", items[i]);
}
```
## While
Python does not have do-while loops that are common to other languages (if you don't know what they are, don't worry about it as it isn't relevant here).
```python
while True:
    # do thing
```
An example is:
```python
i = 0
while i <= 5: # while i is less than or equal to 5
    print(i)
    i += 1 # i = i + 1
```
Bringing if/thens and while loops together:
```python
i = 0
while True:
    print(i)
    if i < 6:
        i += 1
    else:
        break # how you break out of a loop
```
