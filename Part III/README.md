# Chapter 10 - Introducing Python Statements

## Why Indentation Syntax?

Aligning your code according to its logical structure is a major part of making it readable, and thus reusable and maintainable, by yourself and others.

# Chapter 11 - Assignments, Expressions, and Prints

## Extended sequence unpacking

In Python 3.X (only), a new form of sequence assignment allows us to be more flexible in how we select portions of a sequence to assign.

    a, *b = 'spam'

The above code line, for example, matches `a` with the first character in the string on the right and `b` with the rest: `a` is assigned `'s'`, and `b` is assigned `'pam'`. This provides a simpler alternative to assigning the results of manual slicing operations.

A single *starred name*, `*X` can be used in the assignment target in order to specify a more general matching against the sequence - the starred name is assingned a list, which collects all items in the sequence not assigned to other names. This is especially handy for common coding patterns such as splitting a sequence into its "front" and "rest".

    >>> seq = [1, 2, 3, 4]
    >>> a, *b = seq
    >>> a
    1
    >>> b
    [2, 3, 4]

    >>> *a, b = seq
    >>> a
    [1, 2, 3]
    >>> b
    4

    >>> a, *b, c = seq
    >>> a
    1
    >>> b
    [2, 3]
    >>> c
    4

### Boundary cases

1. The starred name may match just a single item, but is always assigned a list:

        >>> seq = [1, 2, 3, 4]
        >>> a, b, c, *d = seq
        >>>print(a, b, c, d)
        1 2 3 [4]

2. If there is nothing left to match the starred name, it is assigned an empty list, regardless of where it appeares:

        >>> a, b, c, d, *e = seq
        >>> print(a, b, c, d, e)
         2 3 4 []

        >>> a, b, *e, c, d = seq
        >>> print(a, b, c, d, e)
        1 2 3 4 []

3. Errors can still be triggered if there is more than one starred name, if there are too few values and no star (as before), and if the starred name is not itself coded inside a sequence:

        >>> a, *b, c, *d = seq
        SyntaxError: two starred expressions in assignment
        
        >>> a, b = seq
        ValueError: too many values to unpack (expected 2)

        >>> *a = seq
        SyntaxError: starred assignment targer must be in a list or tuple

        >>> *a, = seq
        >>> a
        [1, 2, 3, 4]

## Multiple-target assingment and shared references

Keep in mind that there is just one object here, shared by all three variables (they all wind up pointing to the same object in memory). This behaviour is fine for immutable types - for example, when initializing a set of counters to zero.

## Augmented assignment and shared references

This behaviour is usually what we want, but notice that it implies that the `+=` is an *in-place* change for lists; thus, it is not exactly like `+` concatenation, which always makes a *new* object. As for all shared reference case, this difference might matter if other names reference the object being changed:

    >>> L = [1, 2]
    >>> M = L                       # L and M reference the same object
    >>> L = L + [3, 4]              # Concatenation makes a new object
    >>> L, M                        # Changes L but not M
    ([1, 2, 3, 4], [1, 2])

    >>> L = [1, 2]
    >>> M = L
    >>> L += [3, 4]                 # But += really means extend
    >>> L, M                        # M sees the in-place change too!
    ([1, 2, 3, 4], [1, 2, 3, 4])

This only matters for mutables like lists and dictionaries, and it is a fairly obscure case. As always, make copies of your mutable objects if you need to break the shared reference structure.

## Varible Name Rules

- Names that begin with a single underscore (`_X`) are not imported by a `from model import *` statement.
- Names that have two leading and trailing undescores (`__X__`) are system-defined names that have special meaning to the interpreter.
- Names that begin with two underscores and do not end with two more (`__X`) are localized to enclosing classes.
- The name that is just a single underscore (`_`) retains the result of the expression when you are working interactively.

## Print Operations

Along with the standard input and error streams, standard output stream is one of three data connections created when your script starts.

### Call format

    print([object, ...][, sep=' '][,end='\n'][, file=sys.stdout][, flush=false])

In English, this built-in function prints the textual representation of one or more `objects` separated by the string `sep` and followed by the string `end` to the stream `file`, flushing buffered output or not per `flush`.

### Manual stream redirection

In general, `print` and `sys.stdout` are directly related as follows. This statement:

    print(X, Y)

is equivalent to the longer:

    import sys
    sys.stdout.write(str(X) + ' ' + str(Y) + '\n')

Here, we reset `sys.stdout` to a manually opened file named *log.txt*:

    import sys
    sys.stdout = open('log.txt', 'a')       # Redirects prints to a file
    ...
    print(x, y, x)                          # Shows up in log.txt

The `print` operations are happy to keep calling `sys.stdout`'s `write` method, no matter what `sys.stdout` happens to refer to. Because there is just one `sys` module in your process, assigning `sys.stdout` this way will redirect every `print` anywhere in your program.

# Chapter 12 - if Tests and Syntax Rules

## Multiway Branching

You usually code *multiway branching* as a series of `if`/`elif` tests and occasionally by indexing dictionaries or searching lists. Because dictionaries and lists can be buit at runtime dynamically, they are sometimes more flexible that hardcoded `if` logic in scripts:

    >>> branch = {
        'spam': 1.25,
        'ham': 1.99,
        'eggs': 0.99,
    }
    >>> print(branch.get('spam', 'Bad choice'))
    1.25

Though `if`/`elif` tests are perhaps more readable, the potential downside of it is that, short of constructing it as a string and running it with tools like `eval` or `exec`, you cannot construct it at runtimes as easily as a dictionary. In more dynamic programs, data structures offer added flexibility.

## Why You Will Care: Booleans

One common way to use the somewhat unusual behaviour of Python Boolean operators is to select from a set of objects with an `or`:

    X = A or B or C or None

When we define new object types with classes, we can specify their Boolean nature with either the `__bool__` or `__len__` methods. The latter of these is tried if the former is absent and designates false by returning a length of zero.
