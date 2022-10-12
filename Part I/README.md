# Chapter 1 - Python in Questions and Answers

## GUI

Intersting libs:

1. tkinter
2. wxPython
3. Dabo
4. PyQt
5. PyGTK
6. PyWin32 (MFC)
7. IronPython (.NET)
8. Jython (Swing - Java version of Python)

## Internet

Interesting libs:

- HTMLGen - generates HTML from Python classes

Monty-Python refs:

- spam
- eggs
- Brian
- ni
- shrubbery

# Chapter 2 - How Python executes commands

==> Source code *(m.py)* --> Byte-code *(m.pyc)* --> Executing mechanism *(PythonVirtualMachine)*

After version 3.2 compiled python files (.pyc) are saved into the __\_\_pycache\_\___ folder. Their names identifies the Python version in which they were compiled.

Alternative Python Implementations:

- __CPython__ (a standard implementation)
- Jython (Java)
- IronPython (.NET)
- Stackless (parallelism)
- PyPy (faster execution time)

Generaly, all of them replaces two right blocks from the process described above. They compile the source code into the byte-code and executes it on a proper virtual machine.

Another variation of the execution models are:

- Psyco (the first JIT-compiler)
- ShedSkin (Python to C++ translator)
- fixed binary files (executable files)

# Chapter 3 - How user executes commands

To make an executable file from the Python file add  `#!/usr/bin/env python` on the first line of the file and give it rights to execute `chmod+x <filename>`.

`import` operator loads the importing file and gives access to it's content. As the import's final step it executes the imported file's code. And it is done only once per session.

`from` operator copies a name from the module. Formaly, it copies the moduile attributes and they become variables in the accepting side.

Module is a package of variables' names a.k.a __namespace__. And the names inside the package are called __attributes__.
