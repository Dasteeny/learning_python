# Chapter 4 - Introduction into Python's objects types

Python programmes:

1. Programmes consist of modules.
2. Modules contain operators.
3. Operators contain expressions.
4. Expressions create and process objects.

Built-in objects types
| Object Type          | Example                                          |
| -------------------- | ------------------------------------------------ |
| Numbers              | 1234, 3.1415, 3+4j, 0b11, Decimal(), Fraction()  |
| Strings              | 'spam', "Bob's", b'a\x01c', u'sp\xc4m'           |
| Lists                | [1, [2, 'three'], 4.5], list(range(10))          |
| Dictionaries         | {'food': 'spam', 'taste': 'yum'}, dict(hours=10) |
| Tuples               | (1, 'spam', 4, 'U'), tuple('spam'), namedtule    |
| Files                | open('eggs.txt'), open(r'C:\ham.bin'), 'wb'      |
| Sets                 | set('abc'), ('a', 'b', 'c')                      |
| Other main types     | boolean, types themself, None                    |
| Program unit types   | Functions, modules, classes                      |
| Implementation types | Compiled code, stack traceback                   |

## Numbers

    >>> 3.1415 * 2             # repr: as code
    6.2830000000000004
    >>> print(3.1415 * 2)      # str: user-friendly
    6.283

## Strings

Python supports a *raw* string literal that turns off the backslash escape mechanism. Such literals start with the letter *r* and are userful for strings like directory paths (`r'C:\text\new'`).

Python supports coding non-ASCII characters with __\x__  hexadecimal and short __\u__ and long __\U__ Unicode escapes, as well as file-wide encodings declared in program source files.

    >>> 'sp\xc4\u00c4\U000000c4m'
    'spÄÄÄm'

... Unicode processing mostly reduces to transferring text data to and from *files* -- text is *__encoded__* to bytes when stored in a file, and *__decoded__* intop characters (a.k.a code points) when read back into memory.

## Dictionaries - Sorting Keys

`sorted` call returns the result and sorts a variety of object types:

    >>> D
    {'a': 1, 'c': 3, 'b': 2}
    >>> for key in sorted(D):
            print(key, '=>', D[key])
    a => 1
    b => 2
    c => 3

## Iteration and Optimization

An object is *iterable* if it is either a physically stored sequence in memory, or an object that generates one item at a time in the context of an iteration operation -- a sort of "virtual" sequence.

The *generator* comprehension expression is such an object: its values aren't stored in memory all at once, but are produced as requested, usually by iteration tools.

The list comprehension, though, and related functional programming tools like *map* and *filter*, will often run faster than a *for* loop today on some types of code.

## Other Core Types

    >>> X = set('spam')
    >>> Y = {'h', 'a', 'm'}
    >>> X, Y
    {'m', 'a','p', 's'}, {'m', 'a', 'h'})
    >>> X & Y                   # Intersection
    {'m', 'a'}
    >>> X | Y                   # Union
    {'m', 'h', 'a', 'p', 's'}
    >>> X - Y                   # Difference
    {'p', 's'}
    >>> X > Y                   # Superset
    False

# Chapter Summary

An "immutable" object is an object that cannot be changed after it is created. Numbers, strings, and tuples in Python fall into this category.

A "sequence" is a positionally ordered collection of objects. Strings, lists, and tuples are all sequences in Python. They share common sequence operations, such as indexing, concatenation, and slicing, buy also have type-specific method calls.

"Polymorphism" means that the meaning of an operation (like a +) depends on the objects being operated on. This turns out to be a key idea behind using Python well - not constraining code to specific types makes that code automatically applicable to many types.

# Chapter 5 - Numeric Types

|Literal                                |Interpretation                         |
|---------------------------------------|---------------------------------------|
|1234, -24, 0.99999999999999            | Intergers (unlimited size)            |
|1.23, 1., 3.14e-10, 4E210, 4.0e+210    | Floating-point numbers                |
|0o177, 0x9ff, 0b101010                 | Octal, hex, and binary literals       |
|3+4j, 0+4.0j, 3j                       | Complex numbers literals              |
|set('spam'), {1, 2, 3, 4}              | Sets                                  |
|Decimal('1.0'), Fraction(1, 3)         | Decimal and fraction extension types  |
|bool(x), True, False                   | Boolean type and constants            |

## Hex, Octal, Binary: Literals and Conversions

In memory, an integer's value is the same, regardless of the base we use to specify it.

    >>> 0o1, 0o20, 0o377            # Octal literals
    (1, 16, 255)
    >>> 0x01, 0x21, 0xFF            # Hex literals
    (1, 16, 255)
    >>> 0b1, 0b10000, 0b11111111    # Binary literals
    (1, 16, 255)
You can also convert integers to base-specific strings with *string formatting* methgod calls and expressions, which return just digits, not Python literal strings:

    >>> '{0:o}, {1:x}, {2:b}'.format(64, 64, 64) # Numbers=>digits
    '100, 40, 1000000'
    >>> '%o, %x, %x, %X' % (64, 64, 255, 255) # Similar, in all Pythons
    '100, 40, ff, FF'

## Bitwise Operations

As a rule of thumb, if you find yourself wanting to flip bits in Python, you should think about which language you're really coding.

## Fraction Type

The floating-point limitation is especially apparent for values that cannot be represented accurately given their limited number of bits in memory. Both __Fraction__ and __Decimal__ provide ways to get exact results, albeit at the cost of some speed and code verbosity.

    >>> 0.1 + 0.1 + 0.1 - 0.3       # This should be zero (close, but not exact)
    5.551115123125783e-17

    >>> from fractions import Fraction
    >>> Fraction(1, 10) + Fraction(1, 10) + Fraction(1, 10) - Fraction(3, 10)
    Fraction(0, 1)
    
    >>> from decimal import Decimal
    >>> Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')
    Decimal('0.0')

Moreover, fractions and decimals both allow more intuitive and accurate results than floating points sometimes can, in diffent ways - by using rational representation and by limiting precision.

## Fraction conversions and mixed types

To support fraction conversions, floating-point objects now have a method that yields their numerator and denominatior ratio, fractions have a __from_float__ method, and __float__ accepts a __Fraction__ as an argument.

    >>> (2.5).as_integer_ratio()                # float object method
    (5, 2)
    >>> f = 2.5
    >>> z = Fraction(*f.as_integer_ratio())     # Convert float -> fraction: two args
    >>> z                                       # Same as Fraction(5, 2)
    Fraction(5, 2)
    >>> x                                       # x from prior interaction
    Fraction(1, 3)
    >>> x + z
    Fraction(17, 6)                             # 5/2 + 1/3 = 15/6 + 2/6
    >>> float(x)                                # Convert fraction -> float
    0.3333333333333333
    >>> float(z)
    2.5
    >>> float(x + z)
    2.8333333333333335
    >>> 17 / 6
    2.8333333333333335
    >>> Fraction.from_float(1.75)               # Convert float -> fraction: other way
    Fraction(7, 4)
    >>> Fraction(*(1.75).as_integer_ratio())
    Fraction(7, 4)

## Sets

The *set* - an unordered collection of unique and __immutable objects__ that supports opertaions corresponding to mathematical sets.
... although the set expressions shown ealier generally require two sets, their method-based counterparts can often work with *any iterable type* as well:

    >>> S = set([1, 2, 3])
    
    >>> S | set([3, 4])         # Expressions require both to be sets
    set([1, 2, 3, 4])
    >>> S | [3, 4]
    TypeError: unsupported operand type(s) for |: 'set' and 'list'

    >>> S.union([3, 4])         # But their methods allow any iterable
    set([1, 2, 3, 4])
    >>> S.intersection((1, 3, 5))
    set([1, 3])
    >>> S.issubset(range(-5, 5))
    True

## Why sets

Sets can be used to *isolate differences* in lists, strings, and other iterable objects too - simply convert to sets and take the difference - though again the unordered nature of sets means that the results may not match that of the originals:

    >>> set([1, 3, 5, 7]) - set([1, 2, 4, 5, 6])        # Find list differences
    {3, 7}
    >>> set('abcdefg') - set('abdghij')                 # Find string differences
    {'c', 'e', 'f'}
    >>> set('spam') - set(['h', 'a', 'm'])              # Find differences, mixed
    {'p', 's'}
    >>> set(dir(bytes)) - set(dir(bytearray))           # In bytes but not bytearray
    {'__getnewargs__'}
    >>> set(dir(bytearray)) - set(dir(bytes))
    {'append', 'copy', '__alloc__', '__imul__', 'remove', 'pop', 'insert', ...more...]

You can also use sets to perform *order-neutral equality* tests by converting to a set before the test, because order doesn't matter in a set. More formally, two sets are *equal* if and only if every element of each set is contained in the other - that is, each is a subset of the other, regardless of order.

# Chapter 6 - The Dynamic Typing Interlude

In Python, types are determined automatically at runtime, not in response to declarations in your code. This means that you never declare variables ahead of time.

## Variables, Objects, and References

![Assingment schema](../materials/assingment.png)

- *Variables* are entries in a system table, with spaces for links to objects.
- *Objects* are pieces of allocated memory, with enough space to represent the values for which they stand.
- *References* are automatically followed pointers from variables to objects.
  
Technically speaking, objects have more structure than just enough space to represent their values. Each object also has two standard header fields: a *type designator* used to mark the type of the object, and a *reference counter* used to determine when it's OK to reclaim the object.

## Objects Are Garbage-Collected

Whenever a name is assigned to a new object, the space held by the prior object is reclainmed if it is not referenced by any other name or object.

The most immediately tangible benefit of garbage collection is that it means you can use objects liberally without ever needing to allocate or free up space in your script. Python will clean up unused space for you as your program runs. In practice, this eliminates a substantial amout of bookekeeping code required in lower-level languages such as C and C++.

## Shared References

![Shared reference](../materials/shared_object.png)

This scenario in Python - with multiple names referencing the same object - is usually called a *shared reference* (and sometimes just a *shared object*).

    >>> L1 = [2, 3, 4]  # A mutable object
    >>> L2 = L1         # Make a reference to the same object
    >>> L1[0] = 24      # An in-place change

    >>> L1              # List is different
    [24, 3, 4]
    >>> L2              # But so is L2!
    [24, 3, 4]

This behaviour only occurs for mutable objects that support in-place changes, and is usually what you want, but you should be aware of how it works, so that it is expected. It is also just the default: if you don't want such behaviour, you can request that Python *copy* objects instead of making references.

Note that the standard library *copy* module has a call for copying any object type genericallym, as well as a call for copying nested object structures - a dictionary with nested lists, for example:

    import copy
    X = copy.copy(Y)        # Make top-level "shallow" copy of any object Y
    X = copy.deepcopy(Y)    # Make deep copy of any object Y: copy all nested parts

# Chapter 7 - String Fundamentals

Notice that Python displays nonprintable characters in hex, regardless of how they were specified.

If Python does not recognize the character after a \ as being a valid escape code, it simply keeps the backslash in the resulting string:

    >>> x = "C:\py\code"    # Keeps \ literally (displays it as \\)
    >>> x
    'C:\\py\\code'
    >>> len(x)
    10

## Raw Strings Suppress Escapes

If the letter *r* (uppercase or lowercase) appears just before the opening quote of a string, it turns off the escape mechanism. The result is that Python retains your backslashes literally, exactly as you type them.

Besides directory paths on Windows, raw strings are also commonly used for regular expressions. Also note that Python scripts can usually use *forward* slashes in directory paths on Windows and Unix because Python tries to interpret paths portably (i.e., __'C:/new/text.dat'__ worsk when opening files, too). Raw strings are useful if you code paths using native Windows backslashes, though.

## String Conversion Tools

One of Python's design mottos is that it refuses the temptation to guess. As a prime example, you cannot add a number and a string in Python, even if the string looks like a number (i.e., is all digits). This is by design: because + can mean both addition and concatenation, the choice of conversion would be ambiguous. Instead, Python treats this as an error. In Python, magic is generally omitted if it will make your life more complex.

## Changing Strings

Like every operation that yields a new string value, string methods generate new string objects. If you want to retain those objects, you can assign them to variable names. Generating a new string object for each string change is not as inefficient as it may sound.

Because strings are immutable, methods never really change the subject strings in place, even if they are called "replace"!

## Types Share Operation Sets by Categories

More formally, there are three major type (and operation) categories in Python that have this generic nature:

- *Numbers (integers, floating-point, decimal, fraction, others)* - Support addition, multiplication, etc.
- *Sequences (string, lists, tuples)* - Support indexing, slicing, concatenation, etc.
- *Mappings (dictionaries)* - Support indexing by key, etc.

Sets are something of a category unto themselves (they don't map keys to values and are not positionally ordered sequences).

# Chapter 8 - Lists and Dictionaries

> Unlike + concatenation, __append__ doesn't have to generate new objects, so it's usually faster than +, too. You can also mimic __append__ with the clever slice assignments of the prior section: L[len(l):]=[X] is like L.append(X), and L[:0] = [X] is like appending at the front of a list. Both delete an empty slice and insert X, changing L in place quickly, like append. Both are arguably more complex than list methods, though. For instance, L.insert(0, X) can also append an item to the front of a list, and seems noticeably more mnemonic; L.insert(len(L), X) inserts one object at the end too, but unless you like typing, you might as well use L.append(X)!

## Dictionary Usage Notes

- __Sequence operations don't work__
- __Assigning to new indexes adds entries__
- __Keys need not always be strings__ - any *immutable* object can be a dictionary key. For instance, you can use integers as keys, which makes the dictinary look much like a list. Tuples may be used too, allowing compund key values - such as dates and IP addresses - to have associated values. User-defined class instance objects can also be used as keys, as long as they have the proper protocol methods; roughly, they need to tell Python that their values are "hashable" and thus won't change, as otherwise they would be useless as fixed keys. Mutable objects such as lists, sets, and other dictionaries don't work as keys, but are allowed as values.

Provided all the key's values are the same initially, you can also create a dictionary with this special form - simply pass in a list of keys and an initial value for all of the values (the default is __None__):

    >>> dict.fromkeys(['a', 'b'], 0)
    {'a': 0, 'b': 0}

In 3.X the dictionary __keys__, __values__, and __items__ methods return *view objects*, whereas in 2.X they return actual result lists.

View objects are *iterables*, which simply means objects that generate result items one at a time, instead of producing the result list all at once in memory. Besides, being iterable, dictionary views also retain the original order of dictionary components, reflect future changes to the dictionary, and may support set operations. On the other hand, because they are not lists, they do not directly support operations like indexing or the list __sort__ method, and do not display their items as a normal list when printed.

# Chapter 9 - Tuples, Files, and Everything Else

## Tuples syntax peculiarities: Commas and parentheses

Because parentheses can also enclose expressions, you need to do something special to tell Python when a single object in parentheses is a tuple object and not a simple expression. If you really want a single-item tuple, simply add a trailing comma after the single item, before the closing parentheses:

    >>> x = (40)    # An integer!
    >>> x
    40
    >>> y = (40, )  # A tuple containing an integer
    >>> y
    (40, )

## Using Files

- *File iterators are best for reading lines* - Though the reading and writing methods in the table are common, keep in mind that probably the best way to read lines from a text file today is not to read the file at all, files also have an *iterator* that automatically reads one line at a time in a for loop, list comprehension, or other iteration context.
- *Content is strings, not objects*
- *Files are buffered and seekable* - By default, output files are always *buffered*, which means that text you write may not be transferred from memory to disk immediately - closing a file, or running its `flush` method, forces the buffered data to disk. You can avoid buffering with extra `open` arguments, but it may impede performance. Python files are also *random-access* on a byte offset basis - their seek method allows your scripts to jump around to read and write at specific locations.
- *`close` is often optional: auto-close on collection*

If you want to scan a text file line by line, *file iterators* are often your best option:

    >>> for line in open("my_file.txt"):
    ...     print(line, end='')
    ...
    hello text file
    goodbye text file

When coded this way, the temporary file object created by `open` will automatically read and return one line on each loop iteration. This form is usually easiest to code, good on memory use, and may be faster than some other options.

## Text and Binary Files: The Short Story

Python has always supported both text and binary files, but in Python 3.X there is a sharper distinction between the two:

- *Text files* represnt content as normal `str` strings, perform Unicode encoding and decodinng automatically, and perform end-of-line translation by default.
- *Binary files* represent content as a special `bytes` string type and allow programs to access file content unaltered.

You must use `bytes` strings for binary files, and normal `str` strings for text files. Moreover, because text files implement Unicode encodings, you should not open a binary data file in text mode - decoding its content to Unicode text will likely fail.

## Object Flexibility

Empty-limit slices and the dictionary `copy` method only make *top-level* copies; that is, they do not copy nested data structures, if any present. If you need a complete, fully independent copy of a deeply nested data structure use the standard `copy` module:

    import copy
    X = copy.deepcopy(Y)    # Fully copy an arbitrarily nested object Y

__The == operator tests value equivalence.__

__The `is` operator tests object identity.__

## Built-in Type Gotchas

### Repetition Adds One Level Deep

    >>> L = [4, 5, 6]
    >>> X = L * 4       # Like [4, 5, 6] + [4, 5, 6] + ...
    >>> Y = [L] * 4     # [L] + [L] + ... = [L, L, ...]

    >>> X
    [4, 5, 6, 4, 5, 6, 4, 5, 6, 4, 5, 6]
    >>> Y
    [[4, 5, 6], [4, 5, 6], [4, 5, 6], [4, 5, 6]]

Because L was nested in second repetition, Y winds up embedding references back to the original list assigned to L:

    >>> L[1] = 0
    >>> X
    [4, 5, 6, 4, 5, 6, 4, 5, 6, 4, 5, 6]
    >>> Y
    [[4, 0, 6], [4, 0, 6], [4, 0, 6], [4, 0, 6]]

The solution is make copies when you don't want shared references:

    >>> Y = [list(L) * 4]
    >>> L[1] = 0
    >>> Y
    [[4, 5, 6], [4, 5, 6], [4, 5, 6], [4, 5, 6]]

Even more subtly, although Y doesn't share an object with L anymore, it still embeds four references to the same copy of it. If you must avoid that sharing too, you'll want to make sure each embedded copy is unique:

    >>> Y[0][1] = 99
    >>> Y
    [[4, 99, 6], [4, 99, 6], [4, 99, 6], [4, 99, 6]]

    >>> L = [4, 5, 6]
    >>> Y = [list(L) for i in range(4)]
