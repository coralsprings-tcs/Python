# Python Classes
It should be noted that __init__() (pronounced dunder init since it has a double underscore) is how you will usually create a class in Python. Technically the object is created with the __new__ function (which exists whether or not you define it) but that is only necessary to add when you want to affect whether or not an object gets created or affect how they are made. __init__ deals with object instantiation (initialization) and is far more common to be working with.
```python
class Card:
    def __init__(self, suite, number_str):
        self.suite = suite
        self.number = number_str

card_1 = Card('clubs','5')      
print(card_1)           # <__main__.Card object at 0x00000273D1237A50>
card_2 = Card('hearts','J')     
print(card_2)           # <__main__.Card object at 0x00000273D1237AD0>
```
The hexadecimal string that is printed is the memory location of the object. Of course this is not very practical. 

You can overwrite the print behaviour by doing the below with the __str__ (dunder string) function:
```python
class Card:
    def __init__(self, suite, number_str):
        self.suite = suite
        self.number = number_str
    
    def __str__(self):
        return f'{self.number} of {self.suite}'
    
    def draw(self):
        print(f'You drew the {self}') # This will call the __str__ function to represent the card as specified before
    
    def print_quantity(self, number_of_cards):
        print(f'You drew {number_of_cards} "{self}" cards')

card_1 = Card('clubs','5')      
card_2 = Card('hearts','J')  
print(card_1)           # 5 of clubs   
print(card_2)           # J of hearts

# Below are calling the function made for the class, draw. Using self and being attached to the class means you do not need parameters for calling the function.
card_1.draw()           # You drew the 5 of clubs
card_2.draw()           # You drew the J of hearts

# Below is calling a function with a non-self input so needs the appropriate number of paramters outside of self.
card_1.print_quantity(5) # You drew 5 "5 of club" cards
card_2.print_quantity(3) # You drew 3 "J of hearts" cards
```


## Note
In some old Python code you can see something formatted like below:
```python
class Thing(Object):
    def __init__(...):
        # init code
```
This is an old way of making classes that is a holdover from Python2. I do not recommend doing it this way as it is not helpful with code and may be pulled from Python at some point with Python2 being discontinued in ~2019.
