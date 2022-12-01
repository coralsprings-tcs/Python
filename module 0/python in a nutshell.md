# Python in a nutshell
* Python was first released in 1991 by Guido van Rossum. As you can imagine, the name comes from Monty Python (a bloody brilliant British comedy group).
* It is an interpeted scripting/object-oriented language (depending on who you ask).
* Usually in the wild you would see CPython but Pypy is a thing as well as other Python interpreters (including RustPython).
* Some of its defining features are:
    * Using "def" to define a function
    * Its dynamic typing environment (walks like a string, talks like a string, is a string, etc.)
    * Open source nature (free for all from a nonprofit organization)
    * Plain nature in how it defines a lot of stuff unless you really know what you're doing
    * Ease of importing packages (external sources of Python code)
* You may see stuff about Python2. This is its own language for all intents and purposes in how it handles a lot of stuff, especially in the interpreter's structure. Unless noted otherwise, assume I am talking about Python3.
* Here is a sample python script, the obnoxious "hello world".
```python
def say_hello():
    print('Hello world!')

say_hello()
```
* To run it, copy the code into VSCode in a file called hello.py then run it. It will print "Hello world!" to your screen. Easy right?
