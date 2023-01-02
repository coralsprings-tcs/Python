# Object oriented programming
The four principles of OOP are:
* abstraction
* encapsulation
* polymorphism
* inheritance

After looking up what they mean, refer to the below as I will give crude recaps of them and applications:
## Abstraction
An issue that comes from scripts is spaghetti code. You want an object to be as abstract as possible. A good example is a coffee maker. You want it to make coffee but should not have to know how it was made or how it works in order to use it, rather you trust it works and use it.

## Encapsulation
You want to have items in containers. You want attributes and behaviours to be contained in different things. 

## Inheritance
You can have one class inherit from another. Python allows multiple inheritances such as below:
```python
class Vehicle:
    def __init__(self,number_wheels):
        self.number_wheels = number_wheels
        self.__price = 5000 # The single or double underscore here would indicate a private variable in Python, or at least the closest thing to one in it

class Car(Vehicle):
    def __init__(self, can_drive):
        self.number_wheels = 4
        self.can_drive = can_drive
    
    def __str__(self):
        if self.can_drive:
            return 'You have a working car'
        else:
            return 'You have a broken car'
print(Car(True))    # You have a working car
print(Car(0))       # You have a broken car

class Rhombas:
    def __init__(self):
        pass
    
    def draw(self):
        # do action
    # some functions

class Rectangle:
    def __init__(self):
        pass

    def draw(self):
        # do other action
    # other functions

class Square(Rhombas, Rectangle):
    def __init__(self):
        pass

    # you can use functions from Rhombas or Rectangle since a Square is both but the draw function may cause odd behaviour since it will rely on the draw function from the first inherited class (Rhombas for this example) so you'd likely make your own draw function here.
```

## Polymorphism
This relates to abstraction in that you're dealing with trying to have useful functions and behaviours to use. The difference here is you have different parameters for a function of the same name as shown above.
