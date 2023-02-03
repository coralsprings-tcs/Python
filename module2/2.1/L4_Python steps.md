# Python steps
1. Python checks if the name specified is legal (it browses its internal data in order to find an existing function of the name. If this search fails, Python aborts the code).
2. Python checks if the function's requirements for the number of arguments allows you to invoke the function in this way (e.g., if a specific function demands exactly two arguments, any invocation delivering only one argument will be considered erroneous, and will abort the code's execution);
3. Python leaves your code for a moment and jumps into the function you want to invoke; of course, it takes your argument(s) too and passes it/them to the function;
4. The function executes its code, causes the desired effect (if any), evaluates the desired result(s) (if any) and finishes its task;
5. Python returns to your code (to the place just after the invocation) and resumes its execution.
