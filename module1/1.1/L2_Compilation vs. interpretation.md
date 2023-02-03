# Compilation vs. interpretation
## Machine Code
Computers at the most basic level use very small switches, which are turned on and off. They make particular currents, which the hardware can interpret one way or another. This is why it can be interpeted as binary (the base-2 number system), where 1 indicates an "on" state and a 0 an "off" state. Of course using binary to program is not very practical so hexadecimal (base-16) is used. Here is an example for each number system:
* <b>binary</b>: 101010 (may also be written as 0b101010)
* <b>hexadecimal</b>: 2A (may also be written as 0x2A)
* <b>decimal</b>: 42

Hexadecimal is often used to indicate memory addresses (telling the computer where to look for something). Of course, this is not useful to code in, which is where <b>assembly</b> comes in, which is a very low-level language. They are processor-specific so assembly in an Intel computer can be very different than that in an NES or a Samsung Galaxy. Programming in assembly is again not very practical so this is where <b>programming languages</b> come in.

## Programming Language to Machine Code
There are two main ways of transforming a program from a programming language into machine language (assembly):
<table>
<tr>
<td>COMPILATION</td>
<td>The source is translated once an executed through a file containing machine code.</td>
</tr>
<tr>
<td>INTERPRETATION</td>
<td>Anyone using the code will need to translate the source each time it needs to be run using a program. This program is an interpreter.</td>
</tr>
<table>

## Compilation vs. interpretation - advantages and disadvantages
<table>
<thead>
<tr>
<th></th>
<th>COMPILATION</th>
<th>INTERPRETATION</th>
</tr>
</thead>
<tbody>
<tr>
<td>ADVANTAGES</td>
<td>Execution is usually faster. Only the user will need a compiler and any secrets will likely be kept since translated code is stored as machine language.</td>
<td>The code is stored via its programming language, meaning it can be run on computers of different architectures.</td>
</tr>
<tr>
<td>DISADVANTAGES</td>
<td>The compilation can be time-consuming and cannot be run immeditately after editing. It requires as many compilers as hardware platforms the user wants the code to be usable on.</td>
<td>
High speed cannnot be expected as the code shares computer's power with the interpreter. The interpreter is needed to run the code.</td>
</tr>
</tbody>
</table>

## Videos to Watch
* https://www.youtube.com/watch?v=_C5AHaS1mOA
* https://www.youtube.com/watch?v=kil2Z3ij-JA

## Important Note
Python does some bit of compiling. It compiles into Python bytecode, which is what is actually interpreted. This is made every time you run Python and will be updated every time you save a Python file. That is why when you run Python script you may see a .pyc file and/or a pycache folder. For all intents and purposes, Python is considered an interpeted language nonetheless.
