The answers to the previous questions are:

>! Question 1 - True

>! Question 2 - False

>! Question 3 - True

The same applies with float values. If you put in bool(float(0)) you will get False. For any other float number you will get True. This is because of how Python works. All the below will give you true:
```python
bool(5.5) # bool(float)
bool(-21.1) # bool(float)
bool(21) # bool(int)
bool(1) # bool(int)
bool('this is a string') # bool(str)
```
And the below will give you false:
```python
bool(0)
bool(float(0))
bool('')
```
