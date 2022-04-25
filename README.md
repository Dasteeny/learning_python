# learning_python
My highlights and side notes from the M.Lutz - Learning Python book


# Part I

## Chapter 1 - Python in Questions and Answers

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
 

## Chapter 2 - How Python executes commands

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


## Chapter 3 - How user executes commands

To make an executable file from the Python file add  `#!/usr/bin/env python` on the first line of the file and give it rights to execute `chmod+x <filename>`.

`import` operator loads the importing file and gives access to it's content. As the import's final step it executes the imported file's code. And it is done only once per session.

`from` operator copies a name from the module. Formaly, it copies the moduile attributes and they become variables in the accepting side.

Module is a package of variables' names a.k.a __namespace__. And the names inside the package are called __attributes__.


# Part II

## Chapter 4 - Introduction into Python's objects types

Python programmes:
1. Programmes consist of modules.
2. Modules contain operators.
3. Operators contain expressions.
4. Expressions create and process objects.

Built-in objects types
| Object Type   | Example  |
|---|---|
| Numbers  | 1234, 3.1415, 3+4j, 0b11, Decimal(), Fraction()  |
| Strings  | 'spam', "Bob's", b'a\x01c', u'sp\xc4m'  |
| Lists  | [1, [2, 'three'], 4.5], list(range(10))  |
| Dictionaries  | {'food': 'spam', 'taste': 'yum'}, dict(hours=10)  |
| Tuples  | (1, 'spam', 4, 'U'), tuple('spam'), namedtule  |
| Files  | open('eggs.txt'), open(r'C:\ham.bin'), 'wb'  |
| Sets  | set('abc'), ('a', 'b', 'c')  |
| Other main types  | boolean, types themself, None  |
| Program unit types  | Functions, modules, classes  |
| Implementation types  | Compiled code, stack traceback  |

### Numbers
>`>>> 3.1415 * 2             # repr: as code`<br>
>6.2830000000000004<br>
>`>>> print(3.1415 * 2)      # str: user-friendly`<br>
>6.283<br>

### Strings
Python supports a _raw_ string literal that turns off the backslash escape mechanism. Such literals start with the letter _r_ and are userful for strings like directory paths (`r'C:\text\new'`).


Python supports coding non-ASCII characters with **\x**  hexadecimal and short **\u** and long **\U** Unicode escapes, as well as file-wide encodings declared in program source files.
> `>>> 'sp\xc4\u00c4\U000000c4m'` <br>
> 'spÄÄÄm'

... Unicode processing mostly reduces to transferring text data to and from _files_ -- text is **_encoded_** to bytes when stored in a file, and **_decoded_** intop characters (a.k.a code points) when read back into memory. 

### Dictionaries - Sorting Keys
`sorted` call returns the result and sorts a variety of object types:
> `>>> D`<br>
> {'a': 1, 'c': 3, 'b': 2}<br>
> `>>> for key in sorted(D):`<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`print(key, '=>', D[key])`<br>
> a => 1<br>
> b => 2<br>
> c => 3<br>

### Iteration and Optimization
An object is _iterable_ if it is either a physically stored sequence in memory, or an object that generates one item at a time in the context of an iteration operation -- a sort of "virtual" sequence.

The _generator_ comprehension expression is such an object: its values aren't stored in memory all at once, but are produced as requested, usually by iteration tools.

The list comprehensio, though, and related functional programming tools like _map_ and _filter_, will often run faster than a _for_ loop today on some types of code.

### Other Core Types
> `>>> X = set('spam')`<br>
> `>>> Y = {'h', 'a', 'm'}`<br>
> `>>> X, Y`<br>
> ({'m', 'a','p', 's'}, {'m', 'a', 'h'})<br>
> `>>> X & Y`    # Intersection<br>
> {'m', 'a'}<br>
> `>>> X | Y`    # Union<br>
> {'m', 'h', 'a', 'p', 's'}<br>
> `>>> X - Y`    # Difference<br>
> {'p', 's'}
> `>>> X > Y`    # Superset<br>
> False

## Chapter Summary
An "immutable" object is an object that cannot be changed after it is created. Numbers, strings, and tuples in Python fall into this category.

A "sequence" is a positionally ordered collection of objects. Strings, lists, and tuples are all sequences in Python. They share common sequence operations, such as indexing, concatenation, and slicing, buy also have type-specific method calls. 

"Polymorphism" means that the meaning of an operation (like a +) depends on the objects being operated on. This turns out to be a key idea behind using Python well - not constraining code to specific types makes that code automatically applicable to many types.
