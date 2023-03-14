# add -> a + b
# divide -> a / b
# subtract -> a-b
# multiply -> a* b
x= 56
y=98
def add(x,y):
    result = x+y
    return result
def divide(x,y):
    result = x/y
    return result
def subtract(x,y):
    result = x-y
    return result
def multiply(x,y):
    result = x*y
    return result
def exponent(x,y):
    result = x**y
    return result

def operations(x,y,operation):
    try:
        if operation == '+':
            result = add(x,y)
        elif operation == '-':
            result = subtract(x,y)
        elif operation == '*':
            result = multiply(x,y)
        elif operation == '/':
            result = divide(x,y)
        elif operation == '^':
            result = exponent(x,y)
        else:
            result = ''
        print(f'Your result: {result}')
    except:
        print('Invalid input. Try again')


def calculator():
    x = float(input('x: '))
    y = float(input('y: '))
    op = input('Operation: ')
    operations(x,y,op)
#def Fortnite
#Fortnite= 'Give me all your v bucks or ill make you drink the amungus potiosn at 3 am '
calculator()
