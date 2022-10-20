# Compilers vs Interpreters
Watch the below video for a less than 4 minute explanation.
https://www.youtube.com/watch?v=_C5AHaS1mOA

This one adds to it and is less than 3 minutes long.
https://www.youtube.com/watch?v=kil2Z3ij-JA

* Look at how easily you can do a "for" loop in Python vs C.
* The Python interpeter does some "under the hood" stuff so you don't have to do all you would have to do in C.
* As you saw in the first video, interpeters go line by line instead of giving all the instructions at once. 
* Interpeters are much more forgiving than compilers.
* This can be much slower (especially if you have longer scripts).

## How does it work? Crudely explained
* Any compiler will go from source code (the code you write in) to machine code (the code the computer's processor uses) directly.
* Any interpreter will probably be built in some type of code that can be compiled which is then made into machine code. 
* The Python interpeter (python.exe) is built in C so you effectively have to translate from Python to C to what the computer actually uses (machine code).
* Machine code is converted into hexadecimal (base-16, as compared to the decimal / base-10 number system we use) addresses which are made into binary (which turn particular switches in the computer on or off).
* Just in time compilers (JITs) make use of interpeting and compiling so are basically hybrids of compilers and interpreters. Pypy is an example of one and can also be used for coding in Python. We will be making more use of the Python interpreter as it is more standard and is far more forgiving for a lot of cases. When I discuss Python, assume I am referring to the interpreted Python environment (ie. Python.exe made using C).

<b>NOTE</b>: Python does some bit of compiling. It compiles into Python bytecode, which is what is actually interpreted. This is made every time you run Python and will be updated every time you save a Python file. That is why when you run Python script you may see a .pyc file and/or a pycache folder.
