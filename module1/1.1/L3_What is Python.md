# What is Python?
Python is a widely-used, interpreted, object-oriented, and high-level programming language with dynamic semantics, used for general-purpose programming.

## Goals (from Guido van Rossum in 1999)
* An easy and intuitive language just as powerful as those of the major competitors
* Open source, so anyone can contribute to its development
* Code that is as understandable as plain English
* Suitable for everyday tasks, allowing for short development time

The drawbacks are:
* It's not a speed demon – Python does not deliver exceptional performance
* In some cases it may be resistant to some simpler testing techniques – this may mean that debugging Python code can be more difficult than with other language

## Python2 vs 3
Python 2 is an older version of the original Python. Its development has since been intentionally stalled, although that doesn't mean that there are no updates to it. On the contrary, the updates are issued on a regular basis, but they are not intended to modify the language in any significant way.

## Python Interpreters
### CPython
Guido van Rossum used the "C" programming language to implement the very first version of his language and this decision is still in force. All Pythons coming from the PSF are written in the "C" language. There are many reasons for this approach. One of them (probably the most important) is that thanks to it, Python may be easily ported and migrated to all platforms with the ability to compile and run "C" language programs (virtually all platforms have this feature, which opens up many expansion opportunities for Python).

This is why the PSF implementation is often referred to as CPython. This is the most influential Python among all the Pythons in the world.

### Cython
Cython is one of a possible number of solutions to the most painful of Python's traits – the lack of efficiency. Large and complex mathematical calculations may be easily coded in Python (much easier than in "C" or any other traditional language), but the resulting code execution may be extremely time-consuming.

How are these two contradictions reconciled? One solution is to write your mathematical ideas using Python, and when you're absolutely sure that your code is correct and produces valid results, you can translate it into "C". Certainly, "C" will run much faster than pure Python.

This is what Cython is intended to do – to automatically translate the Python code (clean and clear, but not too swift) into "C" code (complicated and talkative, but agile).

### Jython
Another version of Python is called Jython.

"J" is for "Java". Imagine a Python written in Java instead of C. This is useful, for example, if you develop large and complex systems written entirely in Java and want to add some Python flexibility to them. The traditional CPython may be difficult to integrate into such an environment, as C and Java live in completely different worlds and don't share many common ideas.

Jython can communicate with existing Java infrastructure more effectively. This is why some projects find it useful and necessary.

Note: the current Jython implementation follows Python 2 standards. There is no Jython conforming to Python 3, so far.

### Pypy
PyPy - a Python within a Python. In other words, it represents a Python environment written in Python-like language named RPython (Restricted Python). It is actually a subset of Python.

The source code of PyPy is not run in the interpretation manner, but is instead translated into the C programming language and then executed separately.

This is useful because if you want to test any new feature that may be (but doesn't have to be) introduced into mainstream Python implementation, it's easier to check it with PyPy than with CPython. This is why PyPy is rather a tool for people developing Python than for the rest of the users.

This doesn't make PyPy any less important or less serious than CPython, of course.

In addition, PyPy is compatible with the Python 3 language.

## Key Distinction
Python3 is a language and CPython (ie. Python.exe) is an interpreter for the Python language. Assume Python3 and CPython are being used unless said otherwise. Python2 reached end of support last year as well so is considered deprecated.
